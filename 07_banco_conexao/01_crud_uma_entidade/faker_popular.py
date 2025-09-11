from faker import Faker

fake = Faker("pt_BR")

def cadastrar_fakes(session, Pessoa, qtd=5):
    """
    Popula o banco com 'qtd' pessoas falsas.
    
    session: SQLAlchemy session
    Pessoa: classe mapeada da tabela Pessoa
    qtd: número de pessoas a serem criadas
    """
    try:
        for _ in range(qtd):
            nome = fake.name()
            email = fake.email()
            data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90)

            nova_pessoa = Pessoa(
                nome=nome,
                email=email,
                data_nascimento=data_nascimento
            )

            session.add(nova_pessoa)

        session.commit()
        print(f"{qtd} pessoas cadastradas com sucesso usando Faker!")
    except Exception as e:
        print(f"Erro ao cadastrar pessoas fake: {e}")
