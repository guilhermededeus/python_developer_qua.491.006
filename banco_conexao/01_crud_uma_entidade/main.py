# importa a biblioteca sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os 

limpar = lambda: os.system("cls")

def criar_tb_pessoa(engine, Base):
    try:
        class Pessoa(Base):
            __tablename__ = "pessoa"

            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            email = Column(String, nullable=False, unique=True)
            data_nascimento = Column(Date, nullable=False)

        Base.metadata.create_all(engine)

        return Pessoa
    except Exception as e:
        print(f"Não foi possível conectar ao banco. {e}")

def cadastrar_pessoa(session, Pessoa):
    nome = input("Nome: ").strip().title()
    email = input("Email: ").strip().lower()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    nova_pessoa = Pessoa(nome=nome, email=email, data_nascimento=data_nascimento)

    session.add(nova_pessoa)
    session.commit()

    print(f"Pessoa {nome} cadastro com sucesso.")

def listar_pessoas(session, Pessoa):
    pessoas = session.query(Pessoa).all()
    
    print("\nPessoas cadastradas:\n")
    for pessoa in pessoas:
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"Email: {pessoa.email}")
        print(f"Data de nascimneto: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
        print(f"{"-=-"*20}")

def main():
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()

    Pessoa = criar_tb_pessoa(engine, Base)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    while True:
        print(f"{"-=-"*2} CRUD {"-=-"*2}")
        print("[1] Cadastrar pessoa")
        print("[2] Listar pessoas")
        print("[3] Alterar dados de uma pessoa")
        print("[4] Excluir uma pessoa")
        print("[5] Sair do programa")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                cadastrar_pessoa(session, Pessoa)
                continue
            case "2":
                listar_pessoas(session, Pessoa)
                continue
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Programa encerrado!")
                break
            case _:
                print("Opção inválida! Tente novamente.")
                continue
        cadastrar_pessoa(session, Pessoa)

    session.close()


if __name__ == "__main__": 
    main()