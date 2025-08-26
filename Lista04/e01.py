'''Faça um algoritmo para calcular N! (Fatorial de N), sendo que o valor  inteiro de N é fornecido  pelo
usuário.
Sabendo-se que:
N! = 1x2x3x...x(N-1)xN;
0! = 1, por definição'''


n = int(input("Digite um número inteiro: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial = fatorial * i
print(f"O fatorial de {n} é {fatorial}")