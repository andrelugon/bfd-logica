'''Escrever um algoritmo que lê 3 valores a, b, c, e calcula e escreve a média ponderada com peso 5
para o maior dos 3 valores e peso 2.5 para os outros dois'''

a = int(input("Forneça o valor de a: "))
b = int(input("Forneça o valor de b: "))
c = int(input("Forneça o valor de c: "))
if a > b and a > c:
    resultado = ((a * 5) + (b * 2.5) + (c * 2.5))/10
elif b > a and b > c:
    resultado = ((b * 5) + (a * 2.5) + (c * 2.5))/10
else:
    resultado = ((c * 5) + (a * 2.5) + (b * 2.5))/10
print(f"O valor da média ponderada é {resultado}")