nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
media = (nota1 + nota2 + nota3)/3
print(f"A média final é: {media:.1f}")
if (media >= 6):
    print("O aluno está aprovado!")
else:
    print("O aluno está reprovado!")