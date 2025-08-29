# importa a biblioteca sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker 
import entidades as ent
import modulo as md
import faker_popular as fp   # módulo separado só para popular com dados fake

def main():
    # Conexão com o banco
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()

    # Criação/Mapeamento da tabela
    Pessoa = ent.criar_tb_pessoa(engine, Base)
    
    # Sessão
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print(f'{"-=-"*2} CRUD {"-=-"*2}')
        print("[1] Cadastrar pessoa")
        print("[2] Listar pessoas")
        print("[3] Pesquisar pessoas")
        print("[4] Alterar dados de uma pessoa")
        print("[5] Excluir uma pessoa")
        print("[6] Sair do programa")
        print("[7] Popular banco com pessoas fake")  # NOVO
        
        opcao = input("Opção desejada: ").strip()
        md.limpar()

        match opcao:
            case "1":
                md.cadastrar_pessoa(session, Pessoa)
                continue
            case "2":
                md.listar_pessoas(session, Pessoa)
                continue
            case "3":
                md.pesquisar_pessoa(session, Pessoa)
                continue
            case "4":
                print("🚧 Função alterar ainda não implementada.")
                continue
            case "5":
                print("🚧 Função excluir ainda não implementada.")
                continue
            case "6":
                print("Programa encerrado!")
                break
            case "7":
                qtd = input("Quantas pessoas deseja cadastrar? ").strip()
                if qtd.isdigit():
                    fp.cadastrar_fakes(session, Pessoa, int(qtd))
                else:
                    print("Digite um número válido!")
                continue
            case _:
                print("Opção inválida! Tente novamente.")
                continue

    session.close()


if __name__ == "__main__": 
    main()
