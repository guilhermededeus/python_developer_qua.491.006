# Importando bibliotecas.
import os
import time

try:
    Numero = int(input("Informe um número inteiro: "))
    while Numero >= 0:
        os.system("cls")
        print(f"{Numero}...")
        time.sleep(1)
        Numero -= 1
except Exception as e:
    print(f"Não foi possível executar a contagem. {e};")

finally:
    os.system("cls")
    print("BOOOMMMMM!!!")