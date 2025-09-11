import Pessoa
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")
def main():
    # Instância a classe Pessoa
    usuario = Pessoa.Pessoa(nome="", email="", cpf="", idade=0, altura=0.0)
    
    # Inputs
    usuario.nome = input("Nome: ").strip().title()
    usuario.email = input("Email: ").strip().lower()
    usuario.cpf = input("CPF: ").strip()
    usuario.idade = int(input("Idade: "))
    usuario.altura = float(input("Altura: ").replace(",","."))    
    limpar()
    # Output
    print(usuario)

if __name__ == "__main__":
    main()