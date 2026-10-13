"""Testes sem precisar de microfone, TTS real ou acesso à rede."""
import unittest
from unittest.mock import patch
from marvin import voice


class VoiceV03Tests(unittest.TestCase):
    def test_wake_just_marvin(self):
        self.assertEqual(voice.wake_phrase("Marvin"), (True, ""))
        self.assertEqual(voice.wake_phrase("MARVIN!"), (True, ""))
        self.assertEqual(voice.wake_phrase("Mar vim"), (True, ""))

    def test_wake_in_same_sentence(self):
        self.assertEqual(voice.wake_phrase("Marvin, abre o Google"), (True, "abre o google"))

    def test_wake_does_not_match_inside_word(self):
        self.assertEqual(voice.wake_phrase("supermarvin"), (False, ""))

    def test_offline_voice_is_default(self):
        self.assertEqual(voice.OFFLINE_VOICE, "Piper-Faber-ptBR")
        self.assertIn(voice.OFFLINE_VOICE, voice.VOICE_OPTIONS)

    def test_local_tts_first(self):
        with patch("marvin.voice._piper_speak") as local, patch("marvin.voice._edge_speak") as online:
            result = voice.speak("Olá!", voice=voice.OFFLINE_VOICE)
            self.assertIn("Piper", result)
            local.assert_called_once()
            online.assert_not_called()

    def test_fallback_when_piper_is_unavailable(self):
        with patch("marvin.voice._piper_speak", side_effect=RuntimeError("sem modelo")) as local, \
             patch("marvin.voice._edge_speak") as online:
            result = voice.speak("Olá!", voice=voice.OFFLINE_VOICE)
            self.assertIn("AntonioNeural", result)
            local.assert_called_once()
            online.assert_called_once()

    def test_reports_both_tts_errors(self):
        with patch("marvin.voice._piper_speak", side_effect=RuntimeError("sem modelo")), \
             patch("marvin.voice._edge_speak", side_effect=RuntimeError("sem internet")):
            with self.assertRaisesRegex(RuntimeError, "piper:.*edge:"):
                voice.speak("Olá!", voice=voice.OFFLINE_VOICE)


if __name__ == "__main__":
    unittest.main()
