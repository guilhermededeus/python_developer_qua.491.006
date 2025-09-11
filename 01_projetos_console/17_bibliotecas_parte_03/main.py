# Importando bibliotecas.
import math as m

# Exibir o número pi.
print(f"Número pi: {m.pi}.")

# Raiz quadrada.
try:
    Numero = int(input("Informe um número inteiro: "))
    print(f"A raiz quadrada de {Numero} é {m.sqrt(Numero)}.")
except Exception as e:
    print(f"Não foi possível calcular a raiz quadrada. {e}.")

