'''Faça um algoritmo para entrar com dois números e exibir se o primeiro é divisível pelo segundo.'''

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if b == 0:
    print("Não é possível verificar (divisão por zero).")
elif a % b == 0:
    print("O primeiro é divisível pelo segundo")
else:
    print("O primeiro não é divisível pelo segundo")

