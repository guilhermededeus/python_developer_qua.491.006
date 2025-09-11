"""
# TODO - atividade: Crie um programa que recebe do usuário o nome e a idade, e em seguida, mostre um menu de filmes com suas respectivas classificações 
# indicativas e salas de exibição. Exemplo:
- Sala 1: A Roda Quadrada - Livre
- Sala 2: "A Volta dos Que Não Foram" - 12 anos
- Sala 3: Poeira em Alto Mar - 14 anos
- Sala 4: As Tranças do Rei Careca - 16 anos
- Sala 5: A Vingança do Peixe Frito - 18 anos
O usuário deve escolher a sala que está passando o filme que deseja assistir. - Se o usuário tiver a idade mínima ou mais para ver o filme, o programa
 imprime o ingresso com o nome do usuário, a sala, o nome do filme, a data e a hora da compra do ingresso, e deseje bom filme, e em seguida, encerra o programa.
- Se o usuário não tiver a idade mínima para ver o filme, o programa bloqueia a sua entrada, e re-exibe o menu de filmes para que ele escolha outro filme.
"""

import os
import datetime
from datetime import date

Data = date.today().strftime("%d/%m/%y")
Hora = datetime.datetime.now().strftime("%H:%M:%S")

# Filmes das salas.
Sala_1 = "A roda Quadrada"
Sala_2 = "A Volta dos Que Não Foram"
Sala_3 = "Poeira em Alto Mar"
Sala_4 = "As Tranças do Rei Careca"
Sala_5 = "A Vingança do Peixe Frito"

# Tratamento de exceções.
try:
    Nome = input("Informe seu nome: ").title().strip()
    Idade = int(input("Informe sua idade: "))

    while True:
        # Menu.
        print(f"{"-"*20} CINE COBRA {"-"*20}\n")
        print(f"Sala 1 - {Sala_1} - Livre.")
        print(f"Sala 2 - {Sala_2} - 12 anos.")
        print(f"Sala 3 - {Sala_3} - 14 anos.")
        print(f"Sala 4 - {Sala_4} - 16 anos.")
        print(f"Sala 5 - {Sala_5} - 18 anos.\n")

        Sala = input("Informe o número da sala desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")

        match Sala:
            case "1":
                Idade_Minima = 0
                filme = Sala_1
            case "2":
                Idade_Minima = 12
                filme = Sala_2
            case "3":
                Idade_Minima = 14
                filme = Sala_3
            case "4":
                Idade_Minima = 16
                filme = Sala_4
            case "5":
                Idade_Minima = 18
                filme = Sala_5
            case _:
                print("Sala inexistente. Favor escolher outra sala.")
                continue
        if Idade >= Idade_Minima:
            print(f"{"-"*20} INGRESSO CINE COBRA {"-"*20}\n")
            print(f"{filme} - {Idade_Minima}.")
            print(f"Ingresso comprado por {Nome} no dia {Data} às {Hora}.")
            print(f"TENHA UM ÓTIMO FILME!")
            print(f"{"-"*61}")
            break
        else:
            print(f"`{Nome} não possui a idade mínima para assistir {filme}.")
            print("Favor escolher outro filme.")
            continue
                    
except Exception as e:
    print(f"Não foi possível comprar ingresso. {e}.")
