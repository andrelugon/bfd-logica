'''Faça um algoritmo para somar os números pares < 1000 e ao final imprimir o resultado.'''

soma = 0
for i in range(2, 1000, 2):
    soma += i
print("A soma dos números pares menores que 1000 é", soma)