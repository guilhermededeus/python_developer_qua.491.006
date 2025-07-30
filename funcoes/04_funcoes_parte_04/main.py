# importa módulo
from modulo import limpar_tela, velocidade_media, aceleracao_media

# Algoritimo principal
if __name__ == "__main__":
    v = 0
    while True:
        print(f"\n{"-=-"*11}")
        print("[1] - Calcular velocidade média")
        print("[2] - Calcular aceleração média")
        print("[3] - Sair do programa")
        print(f"{"-=-"*11}\n")

        opcao = input("Opção desejada: ").strip()
        limpar_tela()
        match opcao:
            case "1":
                try:
                    vi = float(input("Informe a velocidade inicial: ").replace(",","."))
                    vf = float(input("Informe a velocidade final: ").replace(",","."))

                    v = velocidade_media(vi, vf)
                    limpar_tela()
                    print(f"Velocidade média: {v:.2f}")

                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "2":
                try:
                    t = float(input("Informe o tempo: ").replace(",","."))
                    if v != 0:
                        a = aceleracao_media(v, t)
                        limpar_tela()
                        print(f"Aceleração média: {a:.2f}")
                    else:
                        print("Sem informação da velocidade média.")

                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "3":
                limpar_tela()
                print("Programa finalizado!")
                break
            case _:
                limpar_tela()
                print("Opção inválida! Tente novamente.\n")
                continue
