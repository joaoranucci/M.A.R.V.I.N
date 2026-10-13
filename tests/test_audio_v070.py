import os
from pathlib import Path
import sys
import tempfile
import threading
import types
import unittest
import wave
from unittest.mock import Mock, patch

from marvin import voice


class AudioCancellationTests(unittest.TestCase):
    def test_cancelled_turn_does_not_synthesize_or_fallback(self):
        cancel = threading.Event()
        cancel.set()
        with patch.object(voice, '_piper_speak') as piper, patch.object(voice, '_edge_speak') as edge:
            result = voice.speak('Texto', cancel_event=cancel)
        self.assertEqual(result, 'interrompida')
        piper.assert_not_called()
        edge.assert_not_called()

    def test_cancel_during_synthesis_suppresses_next_engine(self):
        cancel = threading.Event()
        def synthesis(*args):
            cancel.set()
            raise RuntimeError('interrompido')
        with patch.object(voice, '_piper_speak', side_effect=synthesis), patch.object(voice, '_edge_speak') as edge:
            self.assertEqual(voice.speak('Texto', cancel_event=cancel), 'interrompida')
        edge.assert_not_called()

    @unittest.skipUnless(os.name=='nt', 'Windows playback adapter')
    def test_windows_playback_stops_without_waiting_entire_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'test.wav'
            with wave.open(str(path), 'wb') as out:
                out.setnchannels(1)
                out.setsampwidth(2)
                out.setframerate(8000)
                out.writeframes(b'\0\0'*8000)
            token = threading.Event()
            voice._speech_context.cancel = token
            sound = types.SimpleNamespace(PlaySound=Mock(), SND_FILENAME=1, SND_ASYNC=2)
            with patch.dict(sys.modules, {'winsound': sound}), patch.dict(os.environ, {'MARVIN_OUTPUT_DEVICE': ''}), patch('marvin.voice.time.sleep', side_effect=lambda _:token.set()) as wait:
                voice._play_wav(path)
            self.assertEqual(wait.call_count, 1)
            self.assertEqual(sound.PlaySound.call_args.args, (None, 0))
            voice._speech_context.cancel = None

    def test_spoken_output_skips_code_and_links(self):
        result = voice.spoken_text('Resposta ```python\nsecret()\n``` [fonte](https://example.com)')
        self.assertNotIn('secret()', result)
        self.assertNotIn('https://', result)
        self.assertIn('fonte', result)


if __name__=='__main__':
    unittest.main()
