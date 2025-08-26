'''Faça um algoritmo para entrar com um número e informar se ele é divisível por 10, ou é divisível por
5, ou se não é divisível por nenhum destes.'''

n = int(input("Digite um número: "))

if n % 10 == 0:
    print("Divisível por 10")
elif n % 5 == 0:
    print("Divisível por 5")
else:
    print("Não é divisível por 10 nem por 5")
