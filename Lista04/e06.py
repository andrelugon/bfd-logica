'''Faça um algoritmo para ler um valor X e calcular Y = X+2X+3X+4X+5X+…+20X'''

x = int(input("Forneça um valor para x: "))
y = 0

for i in range(1, 21):
    y = y + i * x

print("O valor de Y é", y)
