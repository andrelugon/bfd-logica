'''Tendo como dados de entrada a altura e o sexo de uma pessoa ("M" masculino e "F" feminino),
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
para homens: (72.7*h)-58
para mulheres:(62.1*h)44-7'''

sexo = input("Digite o sexo (M/F): ")
h = float(input("Digite a altura em metros: "))

if sexo == "M" or sexo == "m":
    peso = 72.7 * h - 58
    print("Peso ideal:", peso, "kg")
elif sexo == "F" or sexo == "f":
    peso = 62.1 * h - 44.7
    print("Peso ideal:", peso, "kg")
else:
    print("Sexo inválido.")