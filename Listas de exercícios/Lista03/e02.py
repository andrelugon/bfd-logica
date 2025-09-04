n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
n3 = int(input("Informe o terceiro valor: "))
if (n1 > n2) and (n1 > n3):
    print(f"O número {n1} é o maior valor informado!")
elif (n2 > n1) and (n2 > n3):
    print(f"O número {n2} é o maior valor informado!")
elif (n3 > n1) and (n3 > n2):
    print(f"O número {n3} é o maior valor informado!")
elif (n1 == n2) and (n1 == n3):
    print("Os valores informados são iguais")
else:
    print("Os valores informados são inválidos")