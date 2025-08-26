'''Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o
cargo, conforme a tabela a seguir. Faça um algoritmo que leia o salário e o cargo de um funcionário
e calcule o novo salário. Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber
40% de aumento. Mostre o salário antigo, o novo salário e a diferença.'''

salario = float(input("Digite o salário atual: "))
codigo = int(input("Código do cargo (101/102/103 ou outro): "))

if codigo == 101:
    aumento = 0.10
elif codigo == 102:
    aumento = 0.20
elif codigo == 103:
    aumento = 0.30
else:
    aumento = 0.40

novo_salario = salario * (1 + aumento)
diferenca = novo_salario - salario

print("Salário antigo:", salario)
print("Novo salário:", novo_salario)
print("Diferença:", diferenca)

