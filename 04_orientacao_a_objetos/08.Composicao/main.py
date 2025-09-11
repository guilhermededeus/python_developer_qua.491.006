import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    proprietario = c.Pessoa(nome="", cpf="", email="", telefone="", endereco="")
    carro = c.Veiculo(modelo="", fabricante="", cor="", placa="", ano="",proprietario="")

    # Input
    print("Dados do proprietário:\n")
    proprietario.nome = input("Nome: ").strip().title()
    proprietario.cpf = input("CPF: ").strip()
    proprietario.email = input("Email: ").strip().lower()
    proprietario.telefone = input("Telefone: ").strip()
    proprietario.endereco = input("Endereco: ").strip().title()
    limpar()

    print("Dados do veiculo")
    carro.modelo = input("Modelo: ").strip().title()
    carro.fabricante = input("Fabricante: ").strip().title()
    carro.cor = input("Cor: ").strip()
    carro.placa = input("Placa: ").strip().upper()
    carro.ano = input("Ano: ").strip()
    limpar()
    carro.proprietario = proprietario

    print("Dados do veículo")
    print(f"Modelo: {carro.modelo}")
    print(f"Fabricante: {carro.fabricante}")
    print(f"cor: {carro.cor}")
    print(f"placa: {carro.placa}")
    print(f"ano: {carro.ano}")
    print(f"\nDados do proprietário\n{carro.info_proprietario()}")


if __name__ == "__main__":
    main()