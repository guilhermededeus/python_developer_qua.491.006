from datetime import datetime
import os 

# limpar terminal
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")


def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Digite o nome do usuário: ").strip().title()
        email = input("Digite o e-mail do usuário: ").strip().lower()
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

        nova_pessoa = Pessoa(nome=nome, email=email, data_nascimento=data_nascimento)

        session.add(nova_pessoa)
        session.commit()

        print(f"Pessoa {nome} cadastrada com sucesso.")
    except Exception as e:
        print(f"\nNão foi possível cadastrar pessoa. Erro: {e}")


def listar_pessoas(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        if not pessoas:
            print("\nNenhuma pessoa cadastrada.")
            return

        print("\nPessoas cadastradas:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Data de nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
            print("-" * 30)
    except Exception as e:
        print(f"Não foi possível listar pessoas. Erro: {e}")


def pesquisar_pessoa(session, Pessoa):
    print("Filtrar pessoas por campo")
    print("1 - ID")
    print("2 - Nome")
    print("3 - E-mail")
    print("4 - Data de nascimento")
    print("5 - Retornar")
    
    campo = input("Escolha o campo a ser pesquisado: ").strip()
    limpar()

    pessoas = []  # evita erro caso não caia em nenhum case

    match campo:
        case "1":
            valor = input("Digite o ID para buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.id_pessoa == valor).all()
        case "2":
            valor = input("Digite o nome para buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.nome.like(f"%{valor}%")).all()
        case "3":
            valor = input("Digite o email para buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"%{valor}%")).all()
        case "4":
            valor = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
            try:
                data_nascimento = datetime.strptime(valor, "%d/%m/%Y").date()
                pessoas = session.query(Pessoa).filter(Pessoa.data_nascimento == data_nascimento).all()
            except ValueError:
                print("Data inválida.")
                return
        case "5":
            return
        case _:
            print("Opção inválida")
            return

    limpar()
    print("\nResultado da pesquisa:\n")
    if pessoas:
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
            print("-" * 30)
    else:
        print("Nenhuma pessoa encontrada.")
