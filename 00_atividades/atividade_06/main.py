"""
# TODO - Atividade: Crie um programa em que o usuário informa um ano e o programa exibe todo o calendário  do ano informado pelo usuário.
# NOTE - P usuário poderá informar qualquer napo a partir de 1900.
# NOTE - Use a biblioteca "calendar"
"""

import calendar

# Recebe o ano do usuário
while True:
    try:
        ano = int(input("Informe um ano (a partir de 1900): "))
        if ano >= 1900:
            break
        else:
            print("Por favor, informe um ano igual ou maior que 1900.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Gera e exibe o calendário completo do ano informado
print(f"\n{"-"*24} CALENDÁRIO DO ANO {ano} {"-"*24}\n")
print(calendar.TextCalendar(calendar.SUNDAY).formatyear(ano))
print(f"{"-"*72}")
