'''Faça um algoritmo para calcular a série Fibonacci até o vigésimo termo. A série tem a seguinte forma:
1,1,2,3,5,8,13,21,34,…
A série de Fibonacci é uma sequência em que cada termo é a soma dos dois anteriores, iniciando em 1 e 1.'''

a = 1
b = 1
print(a)
print(b)

for i in range(3, 21):
    c = a + b
    print(c)
    a = b
    b = c