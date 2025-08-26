'''Tendo o consumo diário de uma residência durante um mês (30dias), construa um algoritmo que calcule
e escreva a média consumida por dia.'''

soma = 0
for i in range(1, 4):
    consumo = float(input(f"Consumo do dia {i}: "))
    soma = soma + consumo
media = soma / 30
print(f"Média consumida por dia:", {media})
