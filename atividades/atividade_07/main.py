"""
# TODO - Crie um programa que faça as seguintes operações:
- Cadastrar nome na lista
- Pesquisar por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
- Sair do programa
# NOTE - A lista deve começar vazia. Exemplo: Lista = []
"""

while True:
    nomes = []

    print(f"{"-=-"*2} Banco de Dados {"-=-"*2}")
    print("[1] Cadastrar nome")
    print("[2] Alterar nome")
    print("[3] Excluir nome")
    print("[4] Sair do programa")
    print(f"{"-=-"*13}")

    opcao = int(input("Escolha a opção desejada: "))

    match opcao:
        
        case 1:
            try:
                novo_nome = input("Novo nome: ").title().strip()
                nomes.append(novo_nome)
            except Exception as e:
                print(f"Não foi possível cadastrar o nome. {e}.")
            finally:
                for i in range(len(nomes)):
                    print(f"Índice {i}: {nomes[i]}")

        case 2:
            try:
                ...
            except Exception as e:
                print(f"Não foi possível alterar o nome. {e}.")
            finally:
                ...

        case 3:
            try:
                ...
            except Exception as e:
                print(f"Não foi possível excluir o nome. {e}.")
            finally:
                ...
            
        case 4:
            try:
                ...
            except Exception as e:
                print(f"Não foi sair do programa. {e}.")
            finally:
                ...
                ...

