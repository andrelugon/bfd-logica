'''Para cada nota de compra, tem-se o nome do produto comprado, o valor e o imposto. Faça um
algoritmo que escreva o valor total bruto, o imposto total cobrado e o valor total líquido de todas as
notas. Considere 500 notas'''

total_bruto = 0.0
total_imposto = 0.0
total_liquido = 0.0

for i in range(1, 501):
    produto = input(f"Produto da nota {i}: ")
    valor = float(input("Valor do produto (sem imposto): "))
    imposto = float(input("Imposto (valor): "))
    
    total_bruto += valor + imposto
    total_imposto += imposto
    total_liquido += valor

print("Valor total bruto:", total_bruto)
print("Imposto total:", total_imposto)
print("Valor total líquido:", total_liquido)
