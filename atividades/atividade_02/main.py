"""
# TODO - atividade: Crie um programa que receba do usuário, o nome, o peso em kg, e a altura em metros, e calcule o valor do IMC (Índice de Massa Corporal).
O programa deve mostrar o valor do IMC arredondado para 2 casas decimais, e mostrar o diagnóstico do usuário com base nos seguintes valores:
- Caso o IMC seja menor que 18.5 = abaixo do peso.
- Caso o IMC seja maior ou igual a 18.5 e menor que 25 = peso ideal.
- Caso o IMC seja maior ou igual a 25 e menor que 30 = acima do peso.
- Caso o IMC seja maior ou igual a 30 e menor que 35 = obeso.
- Caso o IMC seja maior ou igual a 35 e menor que 40 = obesidade nível 2.
- Caso o IMC seja maior ou igual a 40 = obesidade mórbida.
# NOTE - o usuário deverá informar o encerramento do programa, ou seja, ele poderá repetir o cálculo quantas vezes quiser.
"""

import os
os.system("cls")

while True:
    try:
        Nome = input("Nome do paciente: ").title()
        Peso = float(input("Peso em KG: ").replace(",","."))
        Altura = float(input("Altura em metros: ").replace(",","."))

        IMC = Peso / (Altura * Altura)

        if Peso < 18.5:
            print(f"{Nome} possui IMC de: {IMC:.2F}.1Abaixo do peso.")
        elif Peso >=18.5 and IMC < 25:
            print(f"{Nome} possui IMC de: {IMC:.2F}. Peso ideal.")
        elif Peso >=25 and IMC < 30:
            print(f"{Nome} possui IMC de: {IMC:.2F}. Acima do peso.")
        elif Peso >=30 and IMC < 35:
            print(f"{Nome} possui IMC de: {IMC:.2F}. Obeso.")
        elif Peso >=35 and IMC < 40:
            print(f"{Nome} possui IMC de: {IMC:.2F}. Obesidade nível 2.")
        elif Peso >=40:
            print(f"{Nome} possui IMC de: {IMC:.2F}. Obesidade mórbida.")

        while True:
            Opcao = input("Deseja executar novamente o programa? [S]im / [N]ão. Opção: ").upper().strip()

            match Opcao:
                case "S":
                    break
                case "N":
                    print("Programa finalizado!")
                    exit()
                case _:
                    print("Opcão inválida.")

    except Exception as e:
        print(f"Não foi executar o programa. {e}.")
        continue