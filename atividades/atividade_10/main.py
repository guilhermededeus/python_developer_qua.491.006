"""
# TODO - atividade: faça um CRUD (Create, Read, Update, Delete) em um JSON.
Opções do menu:
- Criar novo arquivo JSON (usuário irá informar o diretório).
- Abrir arquivo JSON (usuário irá informar o diretório).
- Cadastrar novo usuário em um JSON.
- Listar todos os usuários de um arquivo JSON.
- Pesquisar usuário através do valor de uma chave em um arquivo JSON.
- Alterar dados de um usuário em um arquivo JSON.
- Deletar usuário de um arquivo JSON.
- Sair do programa
Dados do usuário:
- Nome
- Data de nascimento
- CPF
- E-mail
- Telefone
- Filme favorito do usuário
# NOTE - Mostre o nome do arquivo e o diretório no menu
"""
import json
import os

usuarios = []
arquivo = ""
diretorio = "."

while True:
    print(f"\n{'-=-'*4} MENU {'-=-'*4}\n")
    print("[1] Criar arquivo")
    print("[2] Abrir arquivo")
    print("[3] Cadastrar usuário")
    print("[4] Listar usuários")
    print("[5] Pesquisar usuário")
    print("[6] Alterar dados de um usuário")
    print("[7] Deletar um usuário")
    print("[8] Sair do programa")
    print(f"\n{'-=-'*10}\n")
    opcao = input("Opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                nome_arquivo = input("Nome do novo arquivo: ").strip().lower()
                diretorio = input("Diretório onde deseja salvar o arquivo: ").strip()

                if not os.path.exists(diretorio):
                    criar = input(f"Diretório '{diretorio}' não existe. Deseja criá-lo? [S]im / [N]ão: ").strip().lower()
                    if criar == "s":
                        os.makedirs(diretorio)
                        print("Diretório criado com sucesso.")
                    else:
                        print("Voltando ao diretório padrão.")
                        diretorio = "."

                caminho_arquivo = os.path.join(diretorio, f"{nome_arquivo}.json")

                with open(caminho_arquivo, "w", encoding="utf-8") as f:
                    json.dump([], f, ensure_ascii=False, indent=4)

                print(f"Arquivo '{nome_arquivo}.json' criado com sucesso em '{diretorio}'.")
                arquivo = nome_arquivo

            except Exception as e:
                print(f"Erro ao criar o arquivo. {e}")
            continue

        case "2":
            try:
                diretorio = input("Informe o diretório onde o arquivo está salvo: ").strip()
                if not os.path.exists(diretorio):
                    print("Diretório não encontrado. Voltando ao diretório padrão.")
                    diretorio = "."

                arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                caminho_arquivo = f"{diretorio}/{arquivo}.json"

                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    usuarios = json.load(f)

                os.system("cls" if os.name == "nt" else "clear")

                print(f"\nArquivo '{arquivo}.json' carregado com sucesso.")

            except Exception as e:
                print(f"Não foi possível abrir o arquivo JSON. {e}.")
            continue

        case "3":
            try:
                usuario = {}
                usuario['nome'] = input("Informe o nome: ").strip().title()
                usuario['data_nasc'] = input("Informe a data de nascimento: ").strip().replace(".", "/")
                usuario['cpf'] = input("Informe o CPF: ").strip()
                usuario['email'] = input("Informe o e-mail: ").strip().lower()
                usuario['telefone'] = input("Informe o telefone: ").strip()
                usuario['filme'] = input("Informe seu filme favorito: ").strip().title()

                with open(f"{diretorio}/{arquivo}.json", "r", encoding="utf-8") as f:
                    usuarios = json.load(f)

                usuarios.append(usuario)

                with open(f"{diretorio}/{arquivo}.json", "w", encoding="utf-8") as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)

                print("Usuário cadastrado com sucesso!")

            except Exception as e:
                print(f"Erro ao cadastrar usuário. {e}")
            continue

        case "4":
            try:
                with open(f"{diretorio}/{arquivo}.json", "r", encoding="utf-8") as f:
                    usuarios = json.load(f)

                print(f"\n{'-'*20} LISTA DE PESSOAS {'-'*20}\n")
                for usuario in usuarios:
                    for chave in usuario:
                        print(f"{chave.capitalize()}: {usuario.get(chave)}")
                    print("-"*40)

            except Exception as e:
                print(f"Erro ao listar usuários. {e}.")
            continue

        case "5":
            try:
                chave = input("Informe o campo para pesquisa (nome, cpf, email, etc): ").strip().lower()
                valor = input("Informe o valor a ser pesquisado: ").strip()

                with open(f"{diretorio}/{arquivo}.json", "r", encoding="utf-8") as f:
                    usuarios = json.load(f)

                encontrados = []

                for usuario in usuarios:
                    if chave in usuario and str(usuario[chave]).lower() == valor.lower():
                        encontrados.append(usuario)

                if encontrados:
                    print(f"\n{'-'*20} RESULTADOS DA PESQUISA {'-'*20}\n")
                    for usuario in encontrados:
                        for chave_usuario in usuario:
                            print(f"{chave_usuario.capitalize()}: {usuario.get(chave_usuario)}")
                        print("-"*40)
                else:
                    print("Nenhum usuário encontrado com esse critério.")

            except Exception as e:
                print(f"Não foi possível pesquisar. {e}.")
            continue

        case "6":
            try:
                cpf_alvo = input("Informe o CPF do usuário que deseja alterar: ")

                with open(f"{diretorio}/{arquivo}.json", "r", encoding="utf-8") as f:
                    usuarios = json.load(f)

                encontrado = False

                for usuario in usuarios:
                    if usuario["cpf"] == cpf_alvo:
                        print("\nUsuário encontrado: ")
                        for chave in usuario:
                            print(f"{chave.capitalize()}: {usuario.get(chave)}")
                        print("-"*40)

                        usuario['nome'] = input("Informe o nome: ").strip().title()
                        usuario['data_nasc'] = input("Informe a data de nascimento: ").strip().replace(".", "/")
                        usuario['cpf'] = input("Informe o CPF: ").strip()
                        usuario['email'] = input("Informe o e-mail: ").strip().lower()
                        usuario['telefone'] = input("Informe o telefone: ").strip()
                        usuario['filme'] = input("Informe seu filme favorito: ").strip().title()

                        encontrado = True
                        break

                if encontrado:
                    with open(f"{diretorio}/{arquivo}.json", "w", encoding="utf-8") as f:
                        json.dump(usuarios, f, ensure_ascii=False, indent=4)
                    print("Dados atualizados com sucesso.")
                else:
                    print("CPF não encontrado.")

            except Exception as e:
                print(f"Erro ao alterar usuário. {e}.")
            continue

        case "7":
            try:
                cpf_alvo = input("Informe o CPF do usuário que deseja deletar: ").strip()

                encontrado = False

                with open(f"{diretorio}/{arquivo}.json", "r", encoding="utf-8") as f:
                    usuarios = json.load(f)

                for i in range(len(usuarios)):
                    if usuarios[i]["cpf"] == cpf_alvo:
                        del usuarios[i]
                        encontrado = True
                        break

                if encontrado:
                    with open(f"{diretorio}/{arquivo}.json", "w", encoding="utf-8") as f:
                        json.dump(usuarios, f, ensure_ascii=False, indent=4)
                    print("Usuário removido com sucesso.")
                else:
                    print("CPF não encontrado.")

            except Exception as e:
                print(f"Erro ao deletar usuário. {e}.")
            continue

        case "8":
            os.system("cls" if os.name == "nt" else "clear")
            print("Programa encerrado.\n")
            break

        case _:
            print("Opção inválida! Tente novamente.")
            continue
