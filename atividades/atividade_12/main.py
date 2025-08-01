"""
# TODO - Crie um programa que calcule a área e a circuferência de um circulo.
# NOTE - Use lambda
"""
import os
from math import pi
limpar_tela = lambda: os.system("cls" if os.name == "nt" else "clear")
area = lambda r: (pi * r**2)
circuferencia = lambda r: (2 * pi * r)

if __name__ == "__main__":
    while True:
        opcao = input(f"\nRealizar novo cálculo?\n[1] - Sim\n[2] - Não\n\nRespota: ").strip()
        match opcao:
            case "1":
                try:
                    limpar_tela()
                    raio = float(input("Informe o valor do raio: "))
                    r_area = area(raio)
                    r_circuferencia = circuferencia(raio)
                    print(f"Raio: {raio:.2f}")
                    print(f"Área: {r_area:.2f}")
                    print(f"Circuferência: {r_circuferencia:.2f}")

                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "2":
                limpar_tela()
                print("Programa finalizado!")
                break
            case _:
                limpar_tela()
                print("Opção inválida! Tente novamente.")
                continue