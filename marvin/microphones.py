"""Diagnóstico de microfone com teste real de PortAudio, sem chamar Vosk/Gemini."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / '.env')


def main():
    import sounddevice as sd
    from .voice import _input_candidates, _open_microphone
    parser = argparse.ArgumentParser(description='Microfones do MARVIN no Windows')
    parser.add_argument('--test', action='store_true', help='Testa a abertura do microfone por 1,5 segundo')
    args = parser.parse_args()
    print('=== Microfones MARVIN ===')
    print('Dispositivo padrão:', sd.default.device[0])
    hosts = list(sd.query_hostapis())
    for i, d in enumerate(sd.query_devices()):
        if d['max_input_channels'] > 0:
            host = hosts[d['hostapi']]['name']
            print(f" [{i}] {d['name']} | API: {host} | taxa nativa: {d['default_samplerate']} Hz")
    print('\nCandidatos preferidos:',[(i,rate,host) for i,rate,_,host in _input_candidates(sd)][:8])
    if args.test:
        blocks = [0]
        def callback(indata, frames, time_info, status):
            blocks[0] += 1
        try:
            stream, rate = _open_microphone(sd, callback, print)
            try:
                sd.sleep(1500)
            finally:
                stream.stop()
                stream.close()
            if not blocks[0]:
                print('ATENÇÃO: microfone abriu, mas não recebeu pacotes de áudio.')
                return 2
            print(f'OK: microfone abriu e recebeu {blocks[0]} blocos de áudio a {rate} Hz.')
        except Exception as exc:
            print('FALHA:', exc)
            print('Verifique: Configurações do Windows > Privacidade e segurança > Microfone > Permitir aplicativos de desktop.')
            return 1
    print('Se necessário, coloque MARVIN_MIC_DEVICE=NUMERO no .env (preferir dispositivo WASAPI).')
    return 0

if __name__ == '__main__':
    sys.exit(main())
