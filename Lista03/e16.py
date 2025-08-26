'''Um endocrinologista deseja controlar a saúde de seus pacientes e, para isto, se utiliza do índice de
Massa Corporal (IMC). Sabendo-se que o IMC é calculado através da seguinte fórmula: , fazer um
algoritmo que apresente o nome do paciente e sua faixa de risco, baseando-se na seguinte tabela:

INIC                    FAIXA DE RISCO
abaixo de 20            abaixo do peso
a artir de 20 até 25    normal
a artir de 25 até 30    excesso de peso
a artir de 30 até 35    obesidade
acima de 35             obesidade mórbida'''

nome = input("Nome do paciente: ")
peso = float(input("Peso em kg: "))
altura = float(input("Altura em metros: "))

imc = peso / (altura * altura)

if imc < 20:
    faixa = "abaixo do peso"
elif imc < 25:
    faixa = "normal"
elif imc < 30:
    faixa = "excesso de peso"
elif imc <= 35:
    faixa = "obesidade"
else:
    faixa = "obesidade mórbida"

print(f"Paciente: {nome}")
print(f"IMC: {imc:.2f}")
print(f"Faixa de risco: {faixa}")




