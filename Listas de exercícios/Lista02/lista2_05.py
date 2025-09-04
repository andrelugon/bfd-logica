'''
5. Faça um programa que receba o valor de um salário mínimo e o valor do salário de um funcionário, 
calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.
'''
salario_minimo = 1804.00
salario_funcionario = float(input("Informe o valor do salário do funcionário R$ "))
qtd_salario = int(salario_funcionario / salario_minimo)
print(f"O funcionário recebe {qtd_salario} salários mínimos")