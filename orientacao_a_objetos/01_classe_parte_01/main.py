# classe
class Pessoa:
    # Atributos
    nome = "Guilherme"
    idade = 20
    telefone = "(61) 99999-9999"
    cpf = "123.456.789-10"
    email = "guilherme@gmail.com"

    # método
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu e-mail é {self.email}.")


# Programa principal 
if __name__ == "__main__":
    # Instanciar classe
    usuario = Pessoa()

    # Objeto se apresenta
    usuario.apresentar()