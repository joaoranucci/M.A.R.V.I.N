"""Verify API key and test actual Gemini free-tier generation; never print key."""
from pathlib import Path
from dotenv import load_dotenv
from .brain import Brain
from .memory import Memory


def main():
    root = Path(__file__).resolve().parent.parent
    load_dotenv(root / '.env')
    brain = Brain(Memory(root / 'data' / 'marvin.db'))
    print('MARVIN - Diagnostico do Google Gemini (v0.6.2)')
    print('Chave configurada:', 'SIM' if brain.api_key and brain.api_key != 'COLE_SUA_CHAVE_AQUI' else 'NAO')
    print('Modelo preferido:', brain.configured_model)
    print('Em outubro/2026, use uma chave tipo AUTH do AI Studio (Standard antiga nao funciona).')
    print('Modelos com modalidade gratuita:', ', '.join(brain._models()))
    print('\nExecutando teste real de geracao de texto (1 ou 2 chamadas curtas)...')
    print('Confirme no AI Studio que sua chave pertence a um projeto SEM faturamento ativo.')
    print('\n' + brain.diagnose())
    print('\nA chave nao e exibida. Nao envie sua chave ou arquivo .env no chat.')


if __name__ == '__main__':
    main()
