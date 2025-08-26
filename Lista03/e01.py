
'''Faça um algoritmo que leia dois números inteiros positivos e mostre ao final qual deles é o menor.
Caso os números sejam iguais mostre uma mensagem para o usuário informando isso.'''

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
if (n1 < n2):
    print (f"O menor valor informado é {n1}")
elif (n1 > n2):
    print (f"O menor valor informado é {n2}")
else:
    print("Os valores informados são iguais")
