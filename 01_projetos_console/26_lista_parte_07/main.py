# Bibliotecas
import os
import random

# Lista
nomes = []

while True:
    print("[1] Inserir nome na lista")
    print("[2] Exibir lista")
    print("[3] Sortear nome")
    print("[4] Sair do programa")

    opcao = int(input("Informe a opção desejada: ").strip())
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        
        case 1:
            try:
                novo_nome = input("Informe o nome: ").strip().title()
                os.system("cls" if os.name == "nt" else "clear")
                nomes.append(novo_nome)
                print(f"Nome inseirdo com sucesso!")
            except Exception as e:
                print(f"Não foi possível adcionar o nome na lista. {e}.")
            finally:
                continue
        case 2:
            try:
                nomes.sort()
                for nome in nomes:
                    print(nome)
                print(f"-=-"*5)
            except Exception as e:
                print(f"Não foi possível exibir a lista. {e}.")
            finally:
                continue
        case 3:
            i = random.randint(0, len(nomes)-1)
            print(f"Nome sorteado: {nomes[i]}")
            continue
        case 4:
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue
            