"""
# TODO - Crie um programa que faça as seguintes operações:
- Cadastrar nome na lista
- Pesquisar por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
- Sair do programa
# NOTE - A lista deve começar vazia. Exemplo: Lista = []
"""

import os

nomes = []

while True:

    print(f"{"-=-"*1} Banco de Dados {"-=-"*1}")
    print("[1] Mostrar lista")
    print("[2] Cadastrar nome")
    print("[3] Pesquisar nome")
    print("[4] Alterar nome")
    print("[5] Excluir nome")
    print("[6] Sair do programa")
    print(f"{"-=-"*8}")

    opcao = int(input("Escolha a opção desejada: "))

    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case 1:
            if not nomes:
                print("A lista está vazia. Nenhum nome cadastrado.")
            else:
                for i in range(len(nomes)):
                    print(f"Índice {i}: {nomes[i]}")
                    
        case 2:
            try:
                for i in range(len(nomes)):
                    print(f"índice {i}: {nomes[i]}")
                    
                novo_nome = input("Novo nome: ").title().strip()
                nomes.append(novo_nome)
            except Exception as e:
                print(f"Não foi possível cadastrar o nome. {e}.")
            finally:
                continue

        case 3:
            nome_pesquisado = input("Informe o nome a ser pesquisado: ").title().strip()
            os.system("cls" if os.name == "nt" else "clear")
            qtd = nomes.count(nome_pesquisado)
            if qtd == 0:
                print(f"{nome_pesquisado} foi encontado nenhuma vez.")
            elif qtd == 1:
                print(f"{nome_pesquisado} foi encontado {qtd} vez.")
            else:
                print(f"{nome_pesquisado} foi encontado {qtd} vezes.")
        
            continue

        case 4:
            try:
                for i in range(len(nomes)):
                    print(f"índice {i}: {nomes[i]}")
                i = int(input("Informe o novo valor a ser alterado: "))

                if i >= 0 and i < (len(nomes)):
                    nomes[i] = input("Informe o novo valor: ").capitalize().strip()
                    print("Nome alterado com sucesso!") 
                else:
                    print("índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar o item da lista. {e}.")
            finally:
                continue

        case 5:
            try:
                for i in range(len(nomes)):
                    print(f"índice {i}: {nomes[i]}")

                i = int(input("Informe a posição do nome na lista: "))
                if i >= 0 and i < len(nomes):
                    del(nomes[i])
                    print("Nome excluído com sucesso!")
                else:
                    print("Posição inválida.")
            except Exception as e:
                    print(f"Não foi possível excluir o nome da lista. {e}.")
            finally:
                continue
            
        case 6:
           print("Programa encerrado.")
           break

        case _:
            print("Opção inválida.")
            continue
