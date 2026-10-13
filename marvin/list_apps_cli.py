"""Listar apps encontrados. Executar: python -m marvin.list_apps_cli"""
from .windows_control import CATALOG

def main():
    apps = CATALOG.names()
    print(f"MARVIN — {len(apps)} aplicativos e atalhos encontrados\n")
    for app in apps:
        print("  " + app)
    if not apps:
        print("A lista veio vazia. Verifique se você está no Windows com aplicativos no Menu Iniciar.")

if __name__ == "__main__":
    main()
