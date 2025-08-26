#3. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. 
#   Faça um programa que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre a comissão e o salário final do funcionário.

salario = float(input("Forneça o salário: R$ "))
vendas = float(input("Informe o valor das vendas: R$ "))
comissao = float(vendas * 0.04)
salario_final = float(salario + comissao)
print(f"O total de comissão recebido é de R$ {comissao:.2f}")
print(f"O salário total do funcionário é de R$ {salario_final:.2f}")