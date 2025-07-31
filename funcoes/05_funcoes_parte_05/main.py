import modulo as mo

if __name__ == "__main__":
    while True:
        print(f"\n{"-=-"*12}")
        print("[1] - Calcular equecação do 1º grau")
        print("[2] - Calcular equecação do 2º grau")
        print("[3] - Sair do programa")
        print(f"{"-=-"*12}\n")

        opcao = input("Opção desejada: ").strip()
        mo.limpar_tela()
        match opcao:
            case "1":
                try:
                   a = float(input("Informe o valor de A: ").replace(",","."))
                   b = float(input("Informe o valor de B: ").replace(",","."))
                   mo.limpar_tela()
                   x = mo.primeiro_grau(a,b)
                   print(f"O valor de x é {x:.2f}")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "2":
                try:
                   a = float(input("Informe o valor de A: ").replace(",","."))
                   b = float(input("Informe o valor de B: ").replace(",","."))
                   c = float(input("Informe o valor de C: ").replace(",","."))
                   mo.limpar_tela()
                   x = mo.segundo_grau(a,b,c)
                   for result in x:
                        print(f"{result}")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "3":
                mo.limpar_tela()
                print("Programa finalizado!")
                break
            case _:
                mo.limpar_tela()
                print("Opção inválida! Tente novamente.\n")
                continue