"""
# TODO - atividade: Crie um programa que mostre a hora atual sempre sendo atualizada a cada segundo.
# NOTE - para interromper o programa, use a tecla de atalho Ctrl+C
"""

while True:
    import datetime
    from datetime import date
    import time

    hora = datetime.datetime.now().strftime("%H:%M:%S")

    print(f"{hora}.")
    
    time.sleep(1)