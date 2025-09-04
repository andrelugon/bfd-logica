'''Escreva um algoritmo que leia três valores inteiros e mostre-os em ordem decrescente.'''

n1 = int(input("Forneça o primeiro número: "))
n2 = int(input("Forneça o segundo número: "))
n3 = int(input("Forneça o terceiro número: "))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"{n1}, {n2}, {n3}")
    else:
        print(f"{n1}, {n3}, {n2}")
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"{n2}, {n1}, {n3}")
    else:
        print(f"{n1}, {n3}, {n2}")
elif n3 > n2 and n3 > n1:
    if n2 > n1:
        print(f"{n3}, {n2}, {n1}")
    else:
        print(f"{n3}, {n1}, {n2}")
