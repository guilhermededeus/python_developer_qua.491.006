'''
TODO - Crie um programa que faça as seguintes funções:
- Cadastre um novo usuário
- Liste todos os usuários cadastrados
- Altere os dados de um usuário
- Fazer sorteio de um usuário
- Excluir um usuário
- Sair do programa
# NOTE - Dados do usuários:
- Nome completo
- Data de nascimento
- E-mail
- CPF
- Telefone
- Genero
- Data de cadastro (pegar do sistema)
- Nome do cadastro (pegar do sistema)
'''

import datetime
import os
import random

lista = []

while True:
    try:
        dicionario = {}

        print(f"{"-=-"*2} MENU DE OPÇÕES {"-=-"*3}")
        print("[1] Cadastrar novo usuário")
        print("[2] Listar usuários cadastrados")
        print("[3] Alterar dados de um usuário")
        print("[4] Fazer sorteio de um usuário")
        print("[5] Excluir um usuário")
        print("[6] Sair do programa")
        print(f"{"-=-"*10}")

        opcao = input("Operação desejada: ")
        os.system("cls" if os.name == "nt" else "clear")

        match opcao:
            case "1":
                try:
                    dicionario["nome"] = input("Digite o nome completo: ")
                    dicionario["data_nascimento"] = input("Digite a data de nascimento (DD/MM/AAAA): ")
                    dicionario["email"] = input("Digite o e-mail: ")
                    dicionario["cpf"] = input("Digite o CPF: ")
                    dicionario["telefone"] = input("Digite o telefone: ")
                    dicionario["genero"] = input("Digite o gênero: ")
                    dicionario["data_cadastro"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    dicionario["nome_cadastro"] = os.getlogin()
                    lista.append(dicionario)
                    
                    os.system("cls" if os.name == "nt" else "clear")

                    print("Usuário cadastardo!\n")
                    continue

                except Exception as e:
                    print(f"Erro ao cadastrar usuário: {e}")
                    continue

            case "2":
                try:
                    for i in range(len(lista)):
                        print(f"{"-=-"*2} Usuário {i+1} {"-=-"*8}\nNome: {lista[i]['nome']}\nData de Nascimento: {lista[i]['data_nascimento']}\nE-mail: {lista[i]['email']}\nCPF: {lista[i]['cpf']}\nTelefone: {lista[i]['telefone']}\nGênero: {lista[i]['genero']}\nData de Cadastro: {lista[i]['data_cadastro']}\nNome do Cadastro: {lista[i]['nome_cadastro']}\n{"-=-"*12}\n")
                    continue
                except Exception as e:
                    print(f"Não foi possível listar os usuários. {e}.")
                    continue
            case "3":
                    try:
                        if not lista:
                            print("Nenhum usuário cadastrado.\n")
                            continue
                        for i, usuario in enumerate(lista, start=1):
                            print(f"[{i}] {usuario['nome']}")
                        indice = int(input("Informe o número do usuário que deseja alterar: ")) - 1

                        if 0 <= indice < len(lista):
                            print("Deixe em branco para manter o dado atual.\n")
                            for chave in ["nome", "data_nascimento", "email", "cpf", "telefone", "genero"]:
                                novo_valor = input(f"{chave.capitalize().replace('_', ' ')} atual: {lista[indice][chave]} -> Novo valor: ")
                                if novo_valor.strip():
                                    lista[indice][chave] = novo_valor
                            print("Dados atualizados com sucesso!\n")
                        else:
                            print("Usuário inválido.\n")
                    except Exception as e:
                        print(f"Não foi possível alterar os dados. {e}.")
            case "4":
                    try:
                        if not lista:
                            print("Nenhum usuário cadastrado para sorteio.\n")
                            continue
                        sorteado = random.choice(lista)
                        print(f"O usuário sorteado é: {sorteado['nome']} (CPF: {sorteado['cpf']})\n")
                    except Exception as e:
                        print(f"Erro no sorteio: {e}")
            case "5":
                try:
                    if not lista:
                        print("Nenhum usuário cadastrado.\n")
                        continue
                    for i, usuario in enumerate(lista, start=1):
                        print(f"[{i}] {usuario['nome']}")
                    indice = int(input("Informe o número do usuário que deseja remover: ")) - 1

                    if 0 <= indice < len(lista):
                        removido = lista.pop(indice)
                        print(f"O usuário '{removido['nome']}' foi removido.\n")
                    else:
                        print("Índice inválido.\n")
                except Exception as e:
                    print(f"Erro ao excluir usuário: {e}")
            case "6":
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida! Tente novamente.")
                continue    
    except Exception as e:
        print(f"Erro ao exibir o menu: {e}")
        continue