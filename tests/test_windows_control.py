"""Testes de catálogo e roteamento, sem acesso a desktop real."""
import unittest
from unittest.mock import patch
from marvin.windows_control import AppEntry, WindowsAppCatalog
from marvin.commands import detect, execute_local


def catalog():
    return WindowsAppCatalog([
        AppEntry("Discord", "shortcut", "C:/Start/Discord.lnk", "menu/desktop"),
        AppEntry("Google Chrome", "shortcut", "C:/Start/Chrome.lnk", "menu/desktop"),
        AppEntry("Microsoft Edge", "appid", "EdgeTest!App", "Get-StartApps"),
        AppEntry("Visual Studio Code", "shortcut", "C:/Start/VS Code.lnk", "menu/desktop"),
        AppEntry("VALORANT", "shortcut", "C:/Start/VALORANT.lnk", "menu/desktop"),
        AppEntry("Steam", "exe", "C:/Program Files/Steam/steam.exe", "registro"),
        AppEntry("Discord Updater", "shortcut", "C:/Start/Updater.lnk", "menu/desktop"),
    ])


class PcCommandsTests(unittest.TestCase):
    def test_detect_discord(self):
        self.assertEqual(detect("Marvin, abre o Discord").value, "open-app:discord")

    def test_detect_vscode(self):
        self.assertEqual(detect("Marvin, abre o VS Code").value, "open-app:vs code")

    def test_detect_valorant(self):
        self.assertEqual(detect("Marvin, abra o Valorant").value, "open-app:valorant")

    def test_detect_list_refresh(self):
        self.assertEqual(detect("Marvin, liste os aplicativos").value, "list-apps")
        self.assertEqual(detect("Marvin, atualize aplicativos").value, "refresh-apps")

    def test_desktop_commands(self):
        self.assertEqual(detect("Marvin, capture a tela").value, "desktop:screenshot")
        self.assertEqual(detect("Marvin, troque de janela").value, "desktop:alt-tab")
        self.assertEqual(detect("Marvin, aumente o volume").value, "desktop:volume-up")
        self.assertEqual(detect("Marvin, foque no Discord").value, "desktop:focus:discord")
        self.assertEqual(detect("Marvin, feche a janela").value, "desktop:close")

    def test_folder(self):
        self.assertEqual(detect("Marvin, abre a pasta Downloads").value, "folder:downloads")

    def test_no_powershell_injection(self):
        for phrase in ("abra cmd /c format c", "execute powershell apagar arquivos", "abra discord && calc", "abra spotify;shutdown"):
            self.assertEqual(detect(phrase).kind, "ask", phrase)

    def test_catalog_exact_before_prefix(self):
        self.assertEqual(catalog().find("discord").name, "Discord")

    def test_catalog_alias(self):
        self.assertEqual(catalog().find("vs code").name, "Visual Studio Code")
        self.assertEqual(catalog().find("chrome").name, "Google Chrome")
        self.assertEqual(catalog().find("valorante").name, "VALORANT")

    def test_catalog_not_found(self):
        with self.assertRaisesRegex(LookupError, "Não encontrei"):
            catalog().find("aplicativo inexistente")

    def test_catalog_duplicates_prefer_shortcut(self):
        c = WindowsAppCatalog([AppEntry("Discord", "appid", "abc!App"), AppEntry("Discord", "shortcut", "C:/discord.lnk")])
        self.assertEqual(c.find("discord").kind, "shortcut")

    def test_cannot_execute_shell_from_unknown_action(self):
        with self.assertRaises(ValueError):
            execute_local("cmd:dir && rm -rf")

    def test_open_shortcut_uses_startfile_no_shell(self):
        entry = AppEntry("Discord", "shortcut", "C:/Start/Discord.lnk")
        with patch("marvin.windows_control.platform.system", return_value="Windows"), \
             patch("marvin.windows_control.Path.is_file", return_value=True), \
             patch("marvin.windows_control.os.startfile", create=True) as start, \
             patch("marvin.windows_control.subprocess.Popen") as process:
            WindowsAppCatalog._launch(entry)
            start.assert_called_once_with("C:/Start/Discord.lnk")
            process.assert_not_called()

    def test_uwp_does_not_use_shell(self):
        entry = AppEntry("Calc", "appid", "Microsoft.Calc!App")
        with patch("marvin.windows_control.platform.system", return_value="Windows"), \
             patch("marvin.windows_control.subprocess.Popen") as process:
            WindowsAppCatalog._launch(entry)
            process.assert_called_once_with(["explorer.exe", "shell:AppsFolder\\Microsoft.Calc!App"], shell=False)

    def test_list_apps_refresh_without_windows(self):
        c = catalog()
        self.assertIn("Discord", c.names())
        self.assertEqual(len(c.refresh()), 7)


if __name__ == "__main__":
    unittest.main()
