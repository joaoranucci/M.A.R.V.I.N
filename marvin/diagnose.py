"""Verify API key and test actual Gemini free-tier generation; never print key."""
from pathlib import Path
from .config import load_config, VERSION
from .brain import Brain
from .memory import Memory


def main():
    root = Path(__file__).resolve().parent.parent
    data = load_config(root)
    brain = Brain(Memory(data / 'marvin.db'))
    print('MARVIN - Diagnostico IA (v' + VERSION + ')')
    print('Provedor:', brain.provider)
    print('Chave configurada:', 'SIM' if brain.api_key and brain.api_key != 'COLE_SUA_CHAVE_AQUI' else 'NAO')
    print('Modelo preferido:', brain.configured_model)
    print('Modelos configurados:', ', '.join(brain._models()))
    print('\nExecutando teste real de geracao de texto (1 ou 2 chamadas curtas)...')
    print('O teste usa a cota/saldo do provedor configurado.')
    try:
        print('\n' + brain.diagnose())
    finally:
        brain.close()
    print('\nA chave nao e exibida. Nao envie sua chave ou arquivo .env no chat.')


if __name__ == '__main__':
    main()
