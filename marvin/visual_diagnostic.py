from pathlib import Path
import os
from dotenv import load_dotenv
from .visual_agent import VisualAgent,VisualSettings
load_dotenv(Path(__file__).resolve().parent.parent/'.env')

def main():
    print('\n=== MARVIN UI-TARS: DIAGNOSTICO LOCAL ===')
    print(VisualAgent.readiness())
    try:
        c=VisualSettings.from_env()
        print('Modelo:',c.model)
        print('URL:',c.base_url)
        print('Maximo de passos:',c.max_steps)
        print('Atenção: o SDK nao fornece modelo de visao, e configurar URL nao comprova compatibilidade.')
    except RuntimeError as e: print('Configuracao pendente:',e)
if __name__=='__main__':main()
