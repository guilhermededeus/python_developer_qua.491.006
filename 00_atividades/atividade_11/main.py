"""
# TODO - Atividade: crie um programa que receba do usuário um número inteiro e o programa calcula o valor da sequência de Fibonacci.
"""

import modulo as mo

if __name__ == "__main__":
    while True:
        try:
            print(f"{"-=-"*10}")
            print("[1] - Calcular Fibonacci")
            print("[2] - Sair")
            print(f"{"-=-"*10}\n")
            
            opcao = input("Opção: ").strip()
            mo.limpar_tela()
            match opcao:
                    case "1":
                        try:
                            n = int(input("Digite um número intero: "))
                            print(f"O resulto é: {mo.fibonacci(n)}")
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
            print(f"Erro. {e}.\n")
            continue

