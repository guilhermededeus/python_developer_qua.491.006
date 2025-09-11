import os
os.system("cls")

# Tratamento de exceção.
try:
    # Entrada de dado.
    Numero = int(input('Informe um número inteiro: '))

    # Saída de dado.
    print(f'Número informado pelo usuário: {Numero}.')
except Exception as e: # Exception as e (Exibe mensagem de erro).
    print(f"Não foi possível exibir o número. {e}.")
finally: # Exibe uma mensagem indepente do que acontecer no programa.
    print('Programa encerrado com sucesso!')