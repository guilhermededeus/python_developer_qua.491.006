import math as m
import os
os.system("cls")

while True:
    try:
        Raio = float(input("Raio do circulo: "))
        Area = m.pi * Raio**2
        os.system("cls")
        Comprimento_circuferencia = 2 * m.pi * Raio  
        print(f"Área do circulo: {Area:.1f}")
        print(f"Comprimento do circulo: {Comprimento_circuferencia:.1f}")

    
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
        print(f"Não foi possível executar o programa. Erro: {e}")
        continue

"""
# TODO - Atividade: Crie um programa que faça as seguintes operações:
- Calcular área de um círculo;
- Calcular tamanho de uma circuferência;
- Sair do programa.
# NOTE - Para cada loop, o programa deverá limpar o terminal.
"""