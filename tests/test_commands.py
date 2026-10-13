import tempfile
import unittest
from pathlib import Path

from marvin.commands import detect, looks_current, normalize
from marvin.memory import Memory


class CommandTests(unittest.TestCase):
    def test_open_notepad(self):
        self.assertEqual(detect("Marvin, abra o bloco de notas").value, "open-app:bloco de notas")

    def test_open_calc(self):
        self.assertEqual(detect("Abre a calculadora").value, "open-app:calculadora")

    def test_google_search(self):
        command = detect("Marvin, pesquise no Google por Python 3.12")
        self.assertEqual(command.kind, "local")
        self.assertEqual(command.value, "google-browser:python 3.12")

    def test_search_browser(self):
        command = detect("Abra o Google e pesquise por python")
        self.assertEqual(command.value, "google-browser:python")

    def test_unapproved_command_goes_to_ai_not_shell(self):
        command = detect("execute powershell apagar arquivos")
        self.assertEqual(command.kind, "ask")

    def test_current_events(self):
        self.assertTrue(looks_current("Quais são as notícias de hoje?"))
        self.assertFalse(looks_current("O que é Python?"))

    def test_accents(self):
        self.assertEqual(normalize("CALCULADÓRA"), "calculadora")

    def test_memory(self):
        with tempfile.TemporaryDirectory() as directory:
            memory = Memory(Path(directory) / "data.db")
            memory.add_pair("oi", "olá")
            self.assertEqual(memory.recent(), [("user", "oi"), ("model", "olá")])
            memory.clear()
            self.assertEqual(memory.recent(), [])


if __name__ == "__main__":
    unittest.main()
