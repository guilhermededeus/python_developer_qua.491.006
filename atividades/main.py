"""
# TODO - atividade:
# Crie um programa que receba do usuário o valor do etanol e da gasolina em reais, e informe para o 
# usuário qual o melhor combustível para abastecer.
# NOTE - o usuário poderá informar várias vezes os valores, e irá encerrar o programa quando desejar.
# NOTE - compensa etanol caso ele tenha até 70% do valor da gasolina.
# NOTE - DIVIRTAM-SE!!!! =D
"""

import os
os.system("cls")

while True:
# Entrada de dados.
    Etanol = float(input("Valor do etanol: ").replace(",","."))
    Gasolina = float(input("Valor do gasolina: ").replace(",","."))

    Diferenca = Etanol / Gasolina

    if Diferenca <= 0.7:
        print("Compensa abastecer com etanol.")
    else:
        print("Compensa abastecer com gasolina.")
    
    print("Deseja continuar?\n[1] Sim\n[2] Não\n")
    Escolha = input("Escolha: ").strip()

    if Escolha == "1":
        continue
    else:
        print("Programa finalizado!")
        break
