# Importar biblioteca
import os
os.system("cls")

while True:
    Nome = input("Informe seu nome: ")
    os.system("cls")
    print(f"Seja bem-vindo, {Nome}!")

    Prosseguir = input("Deseja inserir outro nome? [S]im / [N]ão. Resposta: ").upper().strip()

    match Prosseguir:
        case "S":
            os.system("cls")
            continue
        case "N":
            break
        case _:
            print("Opção inválida! Tente novamente.")
            continue