"""
# TODO - atividade: Crie um programa que mostre a hora atual sempre sendo atualizada a cada segundo.
# NOTE - para interromper o programa, use a tecla de atalho Ctrl+C
"""


import os
import time
import datetime

# Declaração de variáveis.
while True:
    import datetime
    from datetime import date
    import time

    os.system("cls" if os.name == "nt" else "clear")
    hora = datetime.datetime.now().strftime("%H:%M:%S")

    print(f"Hora atual: {hora}.")
    
    time.sleep(1)