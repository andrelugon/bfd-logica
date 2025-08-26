'''# Faça um algoritmo para calcular um valor a elevado a um expoente b. Os valores a e b deverão ser lidos. Não usar POT(a, b).'''

a = int(input("Digite o valor da base a: "))
b = int(input("Digite o valor do expoente b: "))
resultado = 1
for i in range(1, b + 1):
    resultado = resultado * a
print(f"{a} elevado a {b} é {resultado}")

