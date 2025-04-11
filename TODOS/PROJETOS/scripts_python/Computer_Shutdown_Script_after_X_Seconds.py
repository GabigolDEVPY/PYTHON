import os
import time

def contagem_regressiva_desligamento(segundos):
    while segundos:
        mins, secs = divmod(segundos, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Desligando em: {timer}", end="\r")
        time.sleep(1)
        segundos -= 1

    os.system("shutdown /s /t 1")  # Comando para desligar o computador

# Exemplo: desliga após 30 segundos
contagem_regressiva_desligamento(30)
