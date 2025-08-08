import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    # Instância objeto da classe conta
    cc = c.ContaCorrente(
        titular="",
        cpf="",
        agencia="1010-1",
        conta="10101-1",
        saldo=0.0
    )
    cc.titular = input("Informe seu nome: ").strip()
    cc.cpf = input("Informe seu CPF: ").strip()
    limpar()
    while True:
        print("[1] - Consultar dados")
        print("[2] - Depositar")
        print("[3] - Sacar")
        print("[4] - Sair")
        opcao = input("Informe a opção desejada: ").strip()
        try:
            match opcao:
                case "1":
                    cc.consultar_dados()
                    continue
                case "2":
                    try:
                        valor = float(input("Valor de depósito: R$").replace(",", "."))
                        limpar()
                        if valor > 0:
                            print(f"Depósito efetuado com sucesso!")
                            cc.depositar(valor)
                        else:
                            print("Valor do depósito inválido.")
                    except Exception as e:
                        print(f"Erro ao depositar! {e}.")
                case "3":
                    ...
                case "4":
                    limpar()
                    print("Programa finalizado!")
                    break
                case _:
                    limpar()
                    print("Opção inválida! Tente novamente.")
                    continue
        except Exception as e:
            print(f"Erro. {e}.")
        

if __name__ == "__main__":
    main()