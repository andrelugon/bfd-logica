'''Faça um algoritmo para ler um número entre 1 e 12, e escrever o mês correspondente. Caso o
usuário digite um número fora deste intervalo, deverá aparecer uma mensagem informando que não
existe mês com este número.'''

n = int(input("Digite um número de 1 a 12: "))

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio",
         "Junho", "Julho", "Agosto", "Setembro", "Outubro",
         "Novembro", "Dezembro"]

if 1 <= n <= 12:
    print(meses[n - 1])
else:
    print("Não existe mês com este número")

