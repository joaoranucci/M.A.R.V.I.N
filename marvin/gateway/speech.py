"""Speech synthesis on the PC for devices: Piper Faber (local) or Edge neural voices (online).

Audio is returned to the device and never played on the PC speakers here.
"""
from __future__ import annotations

import asyncio
import io
import threading
import wave

from .. import voice as core_voice

VOICES = [
    {"id": "piper-faber", "label": "Faber · local no PC", "gender": "male", "locale": "pt-BR", "local": True,
     "engine": "piper", "note": "Gerada no PC, sem internet. Primeira síntese carrega o modelo."},
    {"id": "edge-antonio", "label": "Antônio · neural online", "gender": "male", "locale": "pt-BR", "local": False,
     "engine": "edge", "voice": "pt-BR-AntonioNeural",
     "note": "Serviço online da Microsoft usado pelo PC; sem garantia de disponibilidade."},
    {"id": "edge-fabio", "label": "Fábio · neural online", "gender": "male", "locale": "pt-BR", "local": False,
     "engine": "edge", "voice": "pt-BR-FabioNeural", "note": "Serviço online; sem garantia de disponibilidade."},
]
MAX_CHARS = 1200


class SpeechUnavailable(Exception):
    pass


class SpeechService:
    def __init__(self):
        self._lock = threading.Lock()

    def voices(self) -> list[dict]:
        result = []
        for item in VOICES:
            available, reason = True, ""
            if item["engine"] == "piper":
                try:
                    import piper  # noqa: F401
                except ImportError:
                    available, reason = False, "piper-tts não instalado no PC."
                else:
                    if not core_voice.PIPER_MODEL.is_file():
                        available, reason = False, "Modelo Faber ainda não baixado no PC (use TESTAR_VOZ.bat)."
            else:
                try:
                    import edge_tts  # noqa: F401
                except ImportError:
                    available, reason = False, "edge-tts não instalado no PC."
            result.append({k: v for k, v in item.items() if k != "voice"} | {"available": available, "reason": reason or None})
        return result

    def synthesize(self, text: str, voice_id: str, rate: float = 1.0) -> tuple[bytes, str]:
        text = core_voice.spoken_text(str(text))[:MAX_CHARS].strip()
        if not text:
            raise ValueError("Texto vazio para síntese.")
        rate = min(max(float(rate), 0.6), 1.8)
        spec = next((v for v in VOICES if v["id"] == voice_id), None)
        if spec is None:
            raise ValueError("Voz desconhecida.")
        status = next(v for v in self.voices() if v["id"] == voice_id)
        if not status["available"]:
            raise SpeechUnavailable(status["reason"] or "Voz indisponível.")
        with self._lock:
            if spec["engine"] == "piper":
                return self._piper(text, rate), "audio/wav"
            return self._edge(text, spec["voice"], rate), "audio/mpeg"

    @staticmethod
    def _piper(text: str, rate: float) -> bytes:
        from piper import SynthesisConfig
        buffer = io.BytesIO()
        with wave.open(buffer, "wb") as wav_file:
            core_voice._piper_voice().synthesize_wav(text, wav_file, syn_config=SynthesisConfig(
                length_scale=1.03 / rate, noise_scale=.45, noise_w_scale=.6))
        data = buffer.getvalue()
        if len(data) <= 44:
            raise SpeechUnavailable("O Piper gerou áudio vazio.")
        return data

    @staticmethod
    def _edge(text: str, voice: str, rate: float) -> bytes:
        import edge_tts
        percent = int(round((rate - 1.0) * 100))
        chunks: list[bytes] = []

        async def run():
            communicate = edge_tts.Communicate(text, voice, rate=f"{percent:+d}%", pitch="-2Hz")
            async for chunk in communicate.stream():
                if chunk.get("type") == "audio":
                    chunks.append(chunk["data"])

        try:
            asyncio.run(asyncio.wait_for(run(), timeout=25))
        except Exception as exc:  # noqa: BLE001 - network service
            raise SpeechUnavailable("Serviço de voz online indisponível: " + type(exc).__name__) from exc
        data = b"".join(chunks)
        if not data:
            raise SpeechUnavailable("O serviço de voz online devolveu áudio vazio.")
        return data
