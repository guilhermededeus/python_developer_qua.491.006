# classe
class Pessoa:
    # Construtor
    def __init__(self, nome, idade, telefone, cpf, email):
        # Atributos da classe 
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.email = email         

    # Método de ação
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu e-mail é {self.email}."

# Algoritimo principal
if __name__ == "__main__":
    # Instância a classe
    usuario = Pessoa(
        nome="",
        idade=0,
        telefone="",
        cpf="",
        email=""
    )
    try: 
    # Input
        usuario.nome = input("Nome: ").strip().title()
        usuario.idade = int(input("Idade: "))
        usuario.telefone = input("Telefone: ").strip()
        usuario.cpf = input("CPF: ").strip()
        usuario.email = input("Email: ").strip().lower()

        # Chama o método
        print(usuario.apresentar())

    except Exception as e:
        print(f"Error. {e}.")