#4. Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas.
peso = float(input("Informe o peso em Kg:"))
peso_grama = float(peso * 1000)
print(f"O peso de uma pessoa de {peso:.0f} Kg é equivalente a {peso_grama:.0f} gramas.")