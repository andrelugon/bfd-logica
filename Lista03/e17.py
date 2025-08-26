'''Faça um algoritmoq ue obtenha a média e o nome do aluno e mostre ao final qual é o conceito
correspondente. A atribuição de conceitos obedece a tabela abaixo:

Média de aproveitamento     Conceito
>= 9.0                      A
7.5 e < 9.0                 B
6.0 e < 7.5                 C
4.0 e < 6.0                 D
< 4.0                       E
'''

nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

if media >= 9.0:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6.0:
    conceito = "C"
elif media >= 4.0:
    conceito = "D"
else:
    conceito = "E"

print("Aluno:", nome)
print("Média:", media)
print("Conceito:", conceito)