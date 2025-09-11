# Lambda
pa = lambda x: x+2
pg = lambda x: x*2
# Algoritmo principal
if __name__ == "__main__":
    # Lista
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Exibe o pg
    print(f"Progressão Aritmética: {list(map(pa, numeros))}")
    print(f"Progressão Geométrica: {list(map(pg, numeros))}")

