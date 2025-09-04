'''Escrever um algoritmo que lê o número de um vendedor de uma empresa, seu salário fixo e o total
das vendas por ele efetuadas. Sabe-se que cada vendedor recebe um salário fixo, mais uma
comissão proporcional às vendas por ele efetuadas.A comissão é de 3% sobre o total das vendas
até 10.000 e 5% sobre o que ultrapassa este valor. Escrever o número do vendedor, o total de suas
vendas, seu salário fixo e seu salário total.'''

cod_vendedor = int(input("Forneça o número do vendedor: "))
salario_fixo = float(input("Forneça o valor do salário fixo: R$ "))
total_vendas = float(input("Forneça o total da vendas efetuadas: R$ "))
if total_vendas <= 10000:
    comissao = 0.03 * total_vendas
else:
    comissao = (0.03 * 10000) + (0.05 * (total_vendas - 10000))

salario_total = salario_fixo + comissao
print(f"Vendedor nº {cod_vendedor} / Total de vendas: R$ {total_vendas:.2f}  / Salário fixo: R$ {salario_fixo:.2f} / Salário total: R$ {salario_total:.2f}")