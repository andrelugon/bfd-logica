'''Escreva um algoritmo que calcule e escreva a soma dos inteiros pares de 2 a 30.'''

soma = 0
for i in range(2, 31, 2):
    soma = soma + i
print("Soma dos inteiros pares de 2 a 30:", soma)