#2. Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira nota e peso 3 para a segunda nota.

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota1_peso = nota1 * 2
nota2_peso = nota2 * 3
media_ponderada = (nota1_peso + nota2_peso) / (2 + 3)
print(f"A média ponderada entre as notas informadas são: {media_ponderada}")