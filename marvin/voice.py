"""MARVIN: reconhecimento de voz offline e TTS masculino local com fallback.

Windows: Piper Faber pt-BR + winsound como saída principal (sem API),
edge-tts opcional como segunda alternativa. Reconhece a palavra 'Marvin'.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
from functools import lru_cache
from pathlib import Path
import queue
import tempfile
import threading
import time
from urllib.request import Request, urlopen
import wave
import zipfile
import re
from functools import wraps

MODEL_NAME = "vosk-model-small-pt-0.3"
MODEL_URL = f"https://alphacephei.com/vosk/models/{MODEL_NAME}.zip"
ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / MODEL_NAME

PIPER_NAME = "pt_BR-faber-medium"
PIPER_MODEL_DIR = ROOT / "models" / "piper"
PIPER_MODEL = PIPER_MODEL_DIR / f"{PIPER_NAME}.onnx"
PIPER_CONFIG = PIPER_MODEL_DIR / f"{PIPER_NAME}.onnx.json"
PIPER_BASE_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/"
PIPER_SHA256 = "858555e3a064209c57088fe6bd70c4c3dc54d03eaa00c45d5ecaf43a33f95aa7"
OFFLINE_VOICE = "Piper-Faber-ptBR"
MALE_EDGE_VOICES = {"pt-BR-AntonioNeural", "pt-BR-FabioNeural", "pt-BR-HumbertoNeural", "pt-BR-DonatoNeural", "pt-BR-JulioNeural"}
VOICE_OPTIONS = tuple([OFFLINE_VOICE] + sorted(MALE_EDGE_VOICES))
DEFAULT_VOICE = "pt-BR-AntonioNeural"
_playing = threading.Event()
_speech_lock = threading.Lock()
_capture_lock = threading.Lock()
_speech_context = threading.local()
_active_speech = None
_input_level = (0.0, 0.0)
_output_levels = ()
_output_started = 0.0


def _input_meter(pcm):
    global _input_level
    if time.monotonic() - _input_level[0] < .05:
        return
    from array import array
    samples = array('h', pcm)
    level = (sum(x*x for x in samples)/max(1,len(samples)))**.5 / 5000
    _input_level = (time.monotonic(), min(1.0, level))


def _output_meter(samples, rate):
    global _output_levels, _output_started
    import numpy as np
    samples = np.asarray(samples, dtype=np.float32)
    if samples.ndim > 1:
        samples = samples.mean(axis=1)
    size = max(1,int(rate*.04))
    _output_levels = tuple(min(1., float(np.sqrt(np.mean(samples[i:i+size]**2)))/8000)
                           for i in range(0,len(samples),size))
    _output_started = time.monotonic()


def audio_snapshot():
    now = time.monotonic()
    index = max(0,int((now-_output_started)/.04))
    return {'input':_input_level[1] if now-_input_level[0]<.3 else 0.,
            'output':_output_levels[index] if _playing.is_set() and index<len(_output_levels) else 0.}


class SpeechCancel(threading.Event):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def is_set(self):
        return super().is_set() or bool(self.parent and self.parent.is_set())


def is_speaking():
    return _playing.is_set()


def _playback(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        _playing.set()
        try:
            return fn(*args, **kwargs)
        finally:
            _playing.clear()
    return wrapped


def cancel_speech():
    """Stop playback now; synthesis may finish, but its audio is discarded."""
    token = _active_speech
    if token:
        token.set()
    if os.name == "nt":
        try:
            import winsound
            winsound.PlaySound(None, 0)
        except Exception:
            pass


def _cancelled():
    token = getattr(_speech_context, "cancel", None)
    return bool(token and token.is_set())


def spoken_text(text):
    text = re.sub(r"```[\s\S]*?```", " Código disponível na tela. ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", "link na tela", text)
    text = re.sub(r"[*#`|]", "", text)
    return re.sub(r"\s+", " ", text).strip()[:650]


def audio_devices():
    """Inventory only; does not open the microphone or start playback."""
    import sounddevice as sd
    hosts = list(sd.query_hostapis())
    return [{"index": i, "name": d["name"], "host_api": hosts[d["hostapi"]]["name"],
             "input_channels": d["max_input_channels"], "output_channels": d["max_output_channels"],
             "sample_rate": d["default_samplerate"]} for i, d in enumerate(sd.query_devices())]


def _exclusive_capture(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not _capture_lock.acquire(timeout=5):
            raise RuntimeError("O microfone ainda está ocupado. Aguarde o encerramento da captura anterior.")
        try:
            return fn(*args, **kwargs)
        finally:
            _capture_lock.release()
    return wrapped


def wake_phrase(text: str) -> tuple[bool, str]:
    """Verifica se começa por MARVIN, sozinho ou seguido de comando.

    Aceita alguns tokens frequentemente separados pelo Vosk ("mar vim").
    Não ativa em palavras que simplesmente contêm o fragmento marvin.
    """
    from .commands import normalize
    normalized = normalize(text)
    prefixes = (
        "marvin", "mar vim", "marvinh", "marvim", "mar vin",
        "ei marvin", "e marvin", "hey marvin", "ola marvin",
        "ok marvin", "c marvin", "ce marvin", "se marvin", "si marvin",
    )
    # Vosk pode reconhecer nomes próprios de formas diferentes conforme o microfone.
    extra = tuple(a.strip() for a in os.getenv("MARVIN_WAKE_ALIASES", "").split(",") if a.strip())
    prefixes += tuple(normalize(a) for a in extra)
    for prefix in prefixes:
        if normalized == prefix:
            return True, ""
        if normalized.startswith(prefix) and len(normalized) > len(prefix) and normalized[len(prefix)] in " ,:;.!?":
            return True, normalized[len(prefix):].strip(" ,:;.!?")
    return False, ""


def _download(url: str, target: Path, status, *, sha256=None, max_bytes=120_000_000) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_name(target.name + ".part")
    digest = hashlib.sha256()
    total = 0
    last_notice = 0
    try:
        with urlopen(Request(url, headers={"User-Agent": "MARVIN-Windows/0.3"}), timeout=60) as stream, tmp.open("wb") as output:
            while chunk := stream.read(256 * 1024):
                output.write(chunk)
                total += len(chunk)
                digest.update(chunk)
                if total > max_bytes:
                    raise RuntimeError("O arquivo de voz ficou maior que o esperado. Download interrompido.")
                if total - last_notice >= 10_000_000:
                    status(f"Baixando voz local masculina: {total / 1_000_000:.0f} MB recebidos...")
                    last_notice = total
        if not total:
            raise RuntimeError("Download da voz veio vazio.")
        if sha256 and digest.hexdigest().lower() != sha256.lower():
            raise RuntimeError("A verificação SHA-256 da voz não passou; baixe novamente.")
        tmp.replace(target)
    finally:
        tmp.unlink(missing_ok=True)


def ensure_piper_voice(status=lambda message: None) -> Path:
    """Baixa uma única vez o modelo de voz oficial (~63 MB) e seu JSON."""
    if not PIPER_MODEL.is_file():
        status("Baixando a voz masculina Faber (~63 MB), apenas na primeira utilização...")
        _download(PIPER_BASE_URL + PIPER_MODEL.name, PIPER_MODEL, status, sha256=PIPER_SHA256)
    if not PIPER_CONFIG.is_file():
        status("Baixando configuração da voz masculina...")
        _download(PIPER_BASE_URL + PIPER_CONFIG.name, PIPER_CONFIG, status, max_bytes=100_000)
    with PIPER_CONFIG.open("r", encoding="utf-8") as source:
        data = json.load(source)
    if data.get("language", {}).get("code") != "pt_BR":
        raise RuntimeError("Arquivo de configuração de voz inválido (idioma incorreto).")
    return PIPER_MODEL


def ensure_model(status=lambda message: None) -> Path:
    if MODEL_PATH.exists():
        return MODEL_PATH
    models_dir = MODEL_PATH.parent
    models_dir.mkdir(parents=True, exist_ok=True)
    archive = models_dir / (MODEL_NAME + ".zip")
    status("Baixando reconhecimento pt-BR (uma única vez)...")
    _download(MODEL_URL, archive, status, max_bytes=150_000_000)
    status("Extraindo reconhecimento de voz...")
    try:
        with zipfile.ZipFile(archive) as compressed:
            for member in compressed.infolist():
                parts = Path(member.filename).parts
                if not parts or parts[0] != MODEL_NAME or ".." in parts or Path(member.filename).is_absolute():
                    raise RuntimeError("Arquivo do modelo contém caminho inválido.")
            compressed.extractall(models_dir)
        if not MODEL_PATH.exists():
            raise RuntimeError("Modelo de reconhecimento extraído na pasta errada.")
    finally:
        archive.unlink(missing_ok=True)
    return MODEL_PATH


@lru_cache(maxsize=1)
def _model():
    from vosk import Model, SetLogLevel
    SetLogLevel(-1)
    return Model(str(MODEL_PATH))


def _input_settings():
    """Seleciona microfone e taxa. 'auto' privilegia a taxa nativa."""
    device_text = os.getenv("MARVIN_MIC_DEVICE", "").strip()
    device = int(device_text) if device_text.isdecimal() else (device_text or None)
    rate_text = os.getenv("MARVIN_MIC_RATE", "auto").strip().lower()
    if rate_text in ("", "auto"):
        return device, None
    try:
        rate = int(rate_text)
    except ValueError as exc:
        raise RuntimeError("MARVIN_MIC_RATE: use auto, 16000 ou 48000.") from exc
    if rate < 8000 or rate > 96000:
        raise RuntimeError("MARVIN_MIC_RATE fora da faixa de 8000 a 96000.")
    return device, rate


def _input_candidates(sd):
    """Gera alternativas WASAPI/DirectSound para evitar erro PortAudio MME -9999.

    Caso um índice tenha sido informado, só tenta esse dispositivo (e outros
    equivalentes com o mesmo nome), nunca outro microfone sem autorização.
    """
    device, requested_rate = _input_settings()
    devices = list(sd.query_devices())
    hosts = list(sd.query_hostapis())
    inputs = [(i, d) for i, d in enumerate(devices) if d.get("max_input_channels", 0) > 0]
    if not inputs:
        return []
    try:
        default_idx = int(sd.default.device[0])
    except (AttributeError, IndexError, TypeError, ValueError):
        default_idx = -1
    if isinstance(device, int):
        if device < 0 or device >= len(devices) or devices[device].get('max_input_channels', 0) < 1:
            raise RuntimeError(f"MARVIN_MIC_DEVICE={device} não é microfone válido. Rode LISTAR_MICROFONES.bat.")
        reference = str(devices[device]['name']).strip().casefold()
        inputs = [(i, d) for i, d in inputs if i == device or str(d.get('name','')).strip().casefold() == reference]
    elif isinstance(device, str):
        selected = [(i,d) for i,d in inputs if device.casefold() in str(d.get('name','')).casefold()]
        if not selected:
            raise RuntimeError(f"Nenhum microfone corresponde a {device!r}. Rode LISTAR_MICROFONES.bat.")
        inputs = selected
    else:
        default_name = str(devices[default_idx]['name']).strip().casefold() if 0 <= default_idx < len(devices) else ''
        # Derivados de uma mesma entrada podem aparecer repetidos em MME/WASAPI/DirectSound.
        inputs.sort(key=lambda item: 0 if str(item[1].get('name','')).strip().casefold() == default_name else 1)
    def host_name(d):
        try:
            return str(hosts[int(d['hostapi'])]['name']).lower()
        except (IndexError, TypeError, KeyError, ValueError):
            return ''
    def priority(item):
        idx, d = item
        host = host_name(d)
        family = 0 if 'wasapi' in host else 1 if 'directsound' in host else 2 if 'mme' in host else 3
        same = 0 if idx == default_idx else 1
        if device is not None:
            same = 0 if idx == device else 1
        return (family, same) if device is not None else (
            0 if idx == default_idx or (0 <= default_idx < len(devices) and str(d.get('name','')).casefold() == str(devices[default_idx].get('name','')).casefold()) else 1,
            family, same)
    # Prefer WASAPI instead of MME for repeated names. For unknown names,
    # retain the Windows default first; we'll try the alternate next.
    inputs = sorted(inputs, key=priority)
    candidates = []
    for index, info in inputs[:6]:
        try:
            native_rate = int(float(info['default_samplerate']))
        except (KeyError, ValueError, TypeError):
            native_rate = 48000
        rates = list(dict.fromkeys((requested_rate, native_rate, 16000))) if requested_rate else list(dict.fromkeys((native_rate, 16000)))
        for rate in rates:
            if rate and 8000 <= rate <= 96000:
                candidates.append((index, rate, str(info.get('name','Microfone')), host_name(info)))
    return candidates[:12]


def _open_microphone(sd, callback, status=lambda message: None):
    """Open and start a usable stream; caller owns stream.stop()/close()."""
    options = _input_candidates(sd)
    if not options:
        raise RuntimeError("Nenhum dispositivo de entrada encontrado. Conecte e habilite um microfone no Windows.")
    errors = []
    for index, rate, name, host in options:
        stream = None
        try:
            stream = sd.RawInputStream(samplerate=rate, blocksize=0, dtype="int16",
                                       channels=1, device=index, callback=callback)
            stream.start()
            status(f"Microfone: [{index}] {name} ({host}), {rate} Hz")
            return stream, rate
        except Exception as exc:
            errors.append(f"[{index}] {host}/{rate}: {str(exc).splitlines()[0][:110]}")
            if stream is not None:
                try:
                    stream.close()
                except Exception:
                    pass
    raise RuntimeError("O Windows não abriu nenhum microfone testado. "
                       "Execute DIAGNOSTICO_MICROFONE.bat. Verifique Configurações > "
                       "Privacidade e segurança > Microfone > Permitir acesso a aplicativos de desktop. "
                       "Tentativas: " + " | ".join(errors[:3]))


def _new_recognizer(sample_rate, grammar=None):
    from vosk import KaldiRecognizer
    if grammar is None:
        return KaldiRecognizer(_model(), sample_rate)
    return KaldiRecognizer(_model(), sample_rate, json.dumps(grammar, ensure_ascii=False))


@_exclusive_capture
def listen(status=lambda message: None, timeout_seconds=15, cancel_event=None) -> str:
    import sounddevice as sd
    ensure_model(status)
    chunks = queue.Queue(maxsize=32)

    def callback(indata, frames, time_info, status_flags):
        _input_meter(bytes(indata))
        try:
            chunks.put_nowait(bytes(indata))
        except queue.Full:
            pass

    status("Ouvindo... fale agora.")
    stream, sample_rate = _open_microphone(sd, callback, status)
    recognizer = _new_recognizer(sample_rate)
    try:
        end = time.monotonic() + timeout_seconds
        while time.monotonic() < end:
            if cancel_event and cancel_event.is_set():
                return ""
            try:
                block = chunks.get(timeout=0.3)
            except queue.Empty:
                continue
            if recognizer.AcceptWaveform(block):
                text = json.loads(recognizer.Result()).get("text", "").strip()
                if text:
                    return text
        return json.loads(recognizer.FinalResult()).get("text", "").strip()
    finally:
        stream.stop()
        stream.close()


@_exclusive_capture
def listen_wake(on_command, status, stop_event: threading.Event, pause_event: threading.Event, on_wake=None, on_barge=None):
    """Ativa com MARVIN, depois espera comando por 12s.

    Dois reconhecedores: um livre (para "Marvin, abre ...") e um vocabulário
    pequeno para aumentar a chance de identificar a palavra isolada.
    """
    import sounddevice as sd
    ensure_model(status)
    frames = queue.Queue(maxsize=24)

    def callback(indata, frames_count, time_info, flags):
        _input_meter(bytes(indata))
        try:
            frames.put_nowait(bytes(indata))
        except queue.Full:
            pass

    grammar = ["marvin", "mar vim", "ei marvin", "ola marvin", "ok marvin", "[unk]"]
    from .barge_in import SpeechOnset
    from collections import deque
    try:
        threshold = float(os.getenv("MARVIN_BARGE_THRESHOLD", "650"))
    except ValueError:
        threshold = 650
    try:
        import webrtcvad
        use_vad = True
    except ImportError:
        use_vad = False
    onset = SpeechOnset(threshold, use_vad=use_vad)
    preroll = deque()
    preroll_bytes = 0
    interrupted = False
    expecting_command_until = 0.0
    debug_wake = os.getenv("MARVIN_DEBUG_WAKE", "false").strip().lower() == "true"
    was_paused = False
    status("Aguardando 'Marvin'...")
    stream, sample_rate = _open_microphone(sd, callback, status)
    full = _new_recognizer(sample_rate)
    keyword = _new_recognizer(sample_rate, grammar)
    try:
        while not stop_event.is_set():
            try:
                block = frames.get(timeout=0.25)
            except queue.Empty:
                if expecting_command_until and time.monotonic() >= expecting_command_until:
                    expecting_command_until = 0.0
                    status("Aguardando 'Marvin'...")
                continue
            playing = is_speaking()
            barge_enabled = os.getenv("MARVIN_BARGE_IN", "true").lower() == "true"
            try:
                onset.threshold = max(100, min(10000, float(os.getenv("MARVIN_BARGE_THRESHOLD", "650"))))
            except ValueError:
                pass
            detected = onset.feed(block, sample_rate, playing=playing)
            if pause_event.is_set() and not interrupted:
                if playing and barge_enabled and on_barge:
                    preroll.append(block)
                    preroll_bytes += len(block)
                    while preroll_bytes > sample_rate * 2 * .4 and len(preroll) > 1:
                        preroll_bytes -= len(preroll.popleft())
                    if detected:
                        cancel_speech()
                        on_barge()
                        full = _new_recognizer(sample_rate)
                        for previous in preroll:
                            full.AcceptWaveform(previous)
                        preroll.clear()
                        preroll_bytes = 0
                        interrupted = True
                        expecting_command_until = time.monotonic() + 12
                        was_paused = False
                        status("Estou ouvindo você…")
                        continue
                    else:
                        continue
                else:
                    preroll.clear()
                    preroll_bytes = 0
                    was_paused = True
                    continue
            if interrupted and time.monotonic() >= expecting_command_until:
                interrupted = False
                expecting_command_until = 0
                full = _new_recognizer(sample_rate)
                keyword = _new_recognizer(sample_rate, grammar)
                status("Aguardando 'Marvin'...")
                continue
            if interrupted:
                if full.AcceptWaveform(block):
                    sentence = json.loads(full.Result()).get("text", "").strip()
                    if sentence:
                        activated, inline = wake_phrase(sentence)
                        on_command(inline if activated and inline else sentence)
                        interrupted = False
                        expecting_command_until = 0
                continue
            if pause_event.is_set():
                was_paused = True
                continue
            if was_paused:
                # Descarta o audio da propria voz do MARVIN enquanto estava pausado.
                while True:
                    try:
                        frames.get_nowait()
                    except queue.Empty:
                        break
                full = _new_recognizer(sample_rate)
                keyword = _new_recognizer(sample_rate, grammar)
                try:
                    continuity = max(0, min(30, float(os.getenv("MARVIN_CONTINUITY_SECONDS", "0"))))
                except ValueError:
                    continuity = 0
                expecting_command_until = time.monotonic() + continuity if continuity else 0.0
                was_paused = False
            now = time.monotonic()
            if expecting_command_until and now >= expecting_command_until:
                expecting_command_until = 0.0
                status("Aguardando 'Marvin'...")
            final_full = full.AcceptWaveform(block)
            final_wake = keyword.AcceptWaveform(block)
            if not final_full and not final_wake:
                continue
            sentence = json.loads(full.Result()).get("text", "").strip() if final_full else ""
            wake_sentence = json.loads(keyword.Result()).get("text", "").strip() if final_wake else ""
            is_wake, inline = wake_phrase(sentence) if sentence else (False, "")
            if expecting_command_until and sentence and not is_wake:
                pause_event.set()
                on_command(sentence)
                expecting_command_until = 0.0
                continue
            if not is_wake and wake_sentence:
                is_wake, _ = wake_phrase(wake_sentence)
            if debug_wake and (sentence or wake_sentence):
                status(f"O microfone ouviu: {sentence!r} | palavra-chave: {wake_sentence!r}")
            if is_wake:
                if inline:
                    pause_event.set()
                    on_command(inline)
                    expecting_command_until = 0.0
                elif not expecting_command_until:
                    expecting_command_until = now + 12.0
                    status("MARVIN ativado! Diga o comando...")
                    if on_wake:
                        on_wake()

    finally:
        stream.stop()
        stream.close()


@lru_cache(maxsize=1)
def _piper_voice():
    from piper import PiperVoice
    return PiperVoice.load(str(PIPER_MODEL))


@_playback
def _play_wav(path: Path) -> None:
    if _cancelled():
        return
    try:
        import numpy as np
        with wave.open(str(path), 'rb') as wav:
            if wav.getsampwidth() == 2:
                _output_meter(np.frombuffer(wav.readframes(wav.getnframes()),dtype=np.int16).reshape(-1,wav.getnchannels()), wav.getframerate())
    except (ImportError, ValueError, wave.Error):
        pass
    output = os.getenv("MARVIN_OUTPUT_DEVICE", "").strip()
    if output:
        import sounddevice as sd
        with wave.open(str(path), "rb") as wav:
            if wav.getsampwidth() != 2:
                raise RuntimeError("Saída selecionada requer WAV PCM de 16 bits.")
            device = int(output) if output.isdecimal() else output
            with sd.RawOutputStream(samplerate=wav.getframerate(), channels=wav.getnchannels(),
                                    dtype="int16", device=device) as stream:
                while not _cancelled():
                    block = wav.readframes(max(1, wav.getframerate() // 20))
                    if not block:
                        break
                    stream.write(block)
                if _cancelled():
                    stream.abort()
        return
    if os.name == "nt":
        try:
            import winsound
            with wave.open(str(path), "rb") as wav:
                duration = wav.getnframes() / wav.getframerate()
            winsound.PlaySound(str(path), winsound.SND_FILENAME | winsound.SND_ASYNC)
            end = time.monotonic() + duration
            try:
                while time.monotonic() < end and not _cancelled():
                    time.sleep(0.04)
            finally:
                winsound.PlaySound(None, 0)
            return
        except Exception:
            pass
    import pygame
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() and not _cancelled():
            time.sleep(0.04)
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    finally:
        pygame.mixer.quit()


def _piper_speak(text: str, status) -> None:
    ensure_piper_voice(status)
    if _cancelled():
        return
    status("Gerando voz masculina offline...")
    with tempfile.TemporaryDirectory(prefix="marvin_audio_") as directory:
        filepath = Path(directory) / "speech.wav"
        with wave.open(str(filepath), "wb") as wav_file:
            from piper import SynthesisConfig
            _piper_voice().synthesize_wav(text[:1200], wav_file,
                syn_config=SynthesisConfig(length_scale=1.03, noise_scale=.45, noise_w_scale=.6))
        if filepath.stat().st_size <= 44:
            raise RuntimeError("O Piper retornou WAV vazio.")
        status("Reproduzindo voz masculina...")
        _play_wav(filepath)


def _edge_speak(text, voice, status) -> None:
    import edge_tts
    import pygame
    with tempfile.TemporaryDirectory(prefix="marvin_edge_") as directory:
        audio = Path(directory) / "voice.mp3"

        async def generate():
            await edge_tts.Communicate(text[:1600], voice, rate="+0%", pitch="-2Hz").save(str(audio))

        status("Gerando voz neural online...")
        asyncio.run(asyncio.wait_for(generate(), timeout=25))
        if _cancelled():
            return
        if not audio.exists() or not audio.stat().st_size:
            raise RuntimeError("Serviço de voz retornou arquivo vazio.")
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(str(audio))
            try:
                _output_meter(pygame.sndarray.array(pygame.mixer.Sound(str(audio))), pygame.mixer.get_init()[0])
            except Exception:
                pass
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()
            _playing.set()
            status("Reproduzindo áudio...")
            while pygame.mixer.music.get_busy() and not _cancelled():
                time.sleep(0.04)
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        finally:
            _playing.clear()
            pygame.mixer.quit()


def speak(text: str, voice: str | None = None, status=lambda msg: None, cancel_event=None) -> str:
    """Fala em voz masculina e informa qual mecanismo reproduziu a resposta."""
    selected = (voice or os.getenv("MARVIN_VOICE", OFFLINE_VOICE)).strip()
    if selected not in VOICE_OPTIONS:
        raise ValueError("Voz não suportada: " + selected)
    global _active_speech
    text = spoken_text(str(text))
    if not text:
        return "sem texto"
    errors = []
    with _speech_lock:
        token = SpeechCancel(cancel_event)
        _speech_context.cancel = token
        _active_speech = token
        for engine in (["piper", "edge"] if selected == OFFLINE_VOICE else ["edge", "piper"]):
            if token.is_set():
                return "interrompida"
            try:
                if engine == "piper":
                    _piper_speak(text, status)
                    return "interrompida" if token.is_set() else "Piper Faber (offline)"
                else:
                    edge_name = selected if selected in MALE_EDGE_VOICES else "pt-BR-AntonioNeural"
                    _edge_speak(text, edge_name, status)
                    return "interrompida" if token.is_set() else f"{edge_name} (online)"
            except Exception as exc:
                errors.append(f"{engine}: {type(exc).__name__}: {str(exc)[:150]}")
                status(f"Falha em {engine}; tentando alternativa de voz...")
    raise RuntimeError("; ".join(errors))


def test_voice_console() -> None:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
    print("Testando saída de áudio; confira volume do Windows e dispositivo padrão.")
    try:
        used = speak("Olá! Sou o Marvin. Agora você pode me ouvir.", status=print)
        print("SUCESSO ao reproduzir com:", used)
    except Exception as exc:
        print("FALHA:", exc)
        raise


if __name__ == "__main__":
    test_voice_console()
