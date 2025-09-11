import PessoaFisica
import PessoaJuridica
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica.PessoaFisica(email="",telefone="", endereco="",nome="",cpf="",idade="")
    empresa = PessoaJuridica.PessoaJuridica(email="",telefone="", endereco="",razao_social="",nome_fantasia="",cnpj="")

     # Inputs
    usuario.nome = input("Nome: ").strip().title()
    usuario.idade = int(input("Idade: "))
    usuario.cpf = input("CPF: ").strip()
    usuario.telefone = input("Telefone: ")
    usuario.email = input("Email: ").strip().lower()
    usuario.endereco = input("Endereço: ").strip()
    limpar()

    empresa.razao_social = input("Razão social: ").strip().title()
    empresa.nome_fantasia = input("Nome fantasia: ").strip().title()
    empresa.cnpj = input("CNPJ: ").strip()
    empresa.telefone = input("Telefone: ")
    empresa.email = input("Email: ").strip().lower()
    empresa.endereco = input("Endereço: ").strip()
    limpar()

    # Output
    print(f"Dados do usuário\n{usuario}")
    print(f"\nDados da empresa\n{empresa}")

if __name__ == "__main__":
    main()