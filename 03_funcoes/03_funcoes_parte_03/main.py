# Importando módulo
import modulo as m

# Algoritmo principal
if __name__ == "__main__":
    while True:
            # Opções
            print(f"\n{"-=-"*10}")
            print("[1] - Calcular quadrado")
            print("[2] - Calcular retângulo")
            print("[3] - Calcular triângulo")
            print("[4] - Sair")
            print(f"{"-=-"*10}\n")

            # Opção escolhida
            opcao = input("Informe a opção desejada: ").strip()
            match opcao:
                case "1":
                    m.limpar_tela()
                    try:
                        # Entrada de dados
                        lado = float(input("Informe o lado do quadrado: "))
                        # Processamento de dados
                        area = m.area_quadrado(lado)
                        # Saída de dados
                        print(f"Área do quadrado: {area:.2f}")

                    except Exception as e:
                        print(f"Erro. {e}.")
                        continue
                    finally:
                        continue
                case "2":
                    m.limpar_tela()
                    try:
                        # Entrada de dados
                        base = float(input("Informe a base do retângulo: "))
                        altura = float(input("Informe a altura do retângulo: "))
                        # Processamento de dados
                        area = m.area_retangulo(base, altura)
                        # Saída de dados
                        print(f"Área do retângulo: {area:.2f}")
                    except Exception as e:
                        print(f"Erro. {e}.")
                        continue
                    finally:
                        continue
                case "3":
                    m.limpar_tela()
                    try:
                        # Entrada de dados
                        base = float(input("Informe a base do triângulo: "))
                        altura = float(input("Informe a altura do triângulo: "))

                        area = m.area_triangulo(base, altura)

                        print(f"Área do triângulo: {area:.2f}")
                    except Exception as e:
                        print(f"Erro. {e}.")
                        continue
                    finally:
                        continue

                case "4":
                    m.limpar_tela()
                    print("Programa finalizado.")
                    break

                case _:
                    m.limpar_tela()
                    print("Opção inválida! Tente novamente.")
                    continue