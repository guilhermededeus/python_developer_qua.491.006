import modulo as mo

if __name__ == "__main__":
    while True:
        try:
            print(f"{"-=-"*8}")
            print("[1] - Calcular fatorial")
            print("[2] - Sair")
            print(f"{"-=-"*8}\n")
            opcao = input("Opção: ").strip()
            mo.limpar_tela()
            match opcao:
                case "1":
                    try:
                        mo.limpar_tela()
                        n = int(input("Informe um número inteiro: "))
                        print(f"{n}! = {mo.fatorial(n)}\n")
                    except Exception as e:
                        print(f"Erro. {e}.")
                    finally:
                        continue
                case "2":
                    mo.limpar_tela()
                    print("Programa finalizado!")
                    break
                case _:
                    mo.limpar_tela()
                    print("Opção inválida! Tente novamente.\n")
                    continue
        except Exception as e:
            print(f"Erro. {e}.")
            continue