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

usuarios = []

while True:
    try:
        usuario = {}

        print(f"{"-=-"*2} MENU DE OPÇÕES {"-=-"*3}")
        print("[1] Cadastrar novo usuário")
        print("[2] Ver ujsuários cadastrados")
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
                    usuario["nome"] = input("Digite o nome completo: ").strip().title()
                    usuario["data_nascimento"] = input("Digite a data de nascimento (DD/MM/AAAA): ").strip()
                    usuario["email"] = input("Digite o e-mail: ").strip().lower()
                    usuario["cpf"] = input("Digite o CPF: ").strip().lower()
                    usuario["telefone"] = input("Digite o telefone: ").strip()
                    usuario["genero"] = input("Digite o gênero: ").strip()
                    usuario["data_cadastro"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    usuario["nome_cadastro"] = os.getlogin()
                    usuarios.append(usuario)
                    
                    os.system("cls" if os.name == "nt" else "clear")

                    print("Usuário cadastardo!\n")
                    continue

                except Exception as e:
                    print(f"Erro ao cadastrar usuário: {e}")
                    continue

            case "2":
                try:
                    for i in range(len(usuarios)):
                        print(f"{"-=-"*2} Usuário {i+1} {"-=-"*8}\nNome: {usuarios[i]['nome']}\nData de Nascimento: {usuarios[i]['data_nascimento']}\nE-mail: {usuarios[i]['email']}\nCPF: {usuarios[i]['cpf']}\nTelefone: {usuarios[i]['telefone']}\nGênero: {usuarios[i]['genero']}\nData de Cadastro: {usuarios[i]['data_cadastro']}\nNome do Cadastro: {usuarios[i]['nome_cadastro']}\n{"-=-"*12}\n")
                    continue
                except Exception as e:
                    print(f"Não foi possível usuariosr os usuários. {e}.")
                    continue
            case "3":
                    try:
                        if not usuarios:
                            print("Nenhum usuário cadastrado.\n")
                            continue
                        for i, usuario in enumerate(usuarios, start=1):
                            print(f"[{i}] {usuario['nome']}")
                        indice = int(input("Informe o número do usuário que deseja alterar: ")) - 1

                        if 0 <= indice < len(usuarios):
                            print("Deixe em branco para manter o dado atual.\n")
                            for chave in ["nome", "data_nascimento", "email", "cpf", "telefone", "genero"]:
                                novo_valor = input(f"{chave.capitalize().replace('_', ' ')} atual: {usuarios[indice][chave]} -> Novo valor: ")
                                if novo_valor.strip():
                                    usuarios[indice][chave] = novo_valor
                            print("Dados atualizados com sucesso!\n")
                        else:
                            print("Usuário inválido.\n")
                    except Exception as e:
                        print(f"Não foi possível alterar os dados. {e}.")
            case "4":
                    try:
                        if not usuarios:
                            print("Nenhum usuário cadastrado para sorteio.\n")
                            continue
                        sorteado = random.choice(usuarios)
                        print(f"O usuário sorteado é: {sorteado['nome']} (CPF: {sorteado['cpf']})\n")
                    except Exception as e:
                        print(f"Erro no sorteio: {e}")
            case "5":
                try:
                    if not usuarios:
                        print("Nenhum usuário cadastrado.\n")
                        continue
                    for i, usuario in enumerate(usuarios, start=1):
                        print(f"[{i}] {usuario['nome']}")
                    indice = int(input("Informe o número do usuário que deseja remover: ")) - 1

                    if 0 <= indice < len(usuarios):
                        removido = usuarios.pop(indice)
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