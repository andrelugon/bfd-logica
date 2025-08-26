'''Leia 200 valores reais e escreva o seu somatório.'''

soma = 0.0
for i in range(1, 201):
    valor = float(input(f"Digite o {i}º valor: "))
    soma += valor
print("Somatório dos 200 valores:", soma)