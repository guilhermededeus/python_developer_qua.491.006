import os
os.system("cls")  

# declaração de variáveis
x = 10
y = 5

"""""
# convertendo números para string para concatenação de subtração
resultado = 5
x = str(x)  # Convertendo x para string
y = str(y)  # Convertendo y para string
resultado = str(resultado)  # Convertendo resultado para string

# operações 
print("A soma dos valores de ", x, "e", y, "é", x+y,".")    # Adição
print("A subtração dos valores de " + x + " e " + y + " é " + resultado +" .") # Subtração
"""
soma = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y
resto = x%y
potencia = x**y

print("A soma de {} e {} é {}.".format(x, y, soma))
print(f"A subtração de {x} e {y} é {subtracao}.")
print(f"A multiplicação de {x} e {y} é {multiplicacao}.")
print(f"A divisão de {x} e {y} é {divisao:.2f}.")  
print(f"O resto da divisão de {x} e {y} é {resto}.")
print(f"{x} elevado a {y} é {potencia:.2f}.")
