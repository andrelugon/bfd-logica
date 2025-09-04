n1 = int(input("Informe o número: "))
if (n1 % 2 == 0) and ((n1 > 0) and (n1 != 0)):
    print("O número informado é par e positivo!")
elif (n1 % 2 == 0) and ((n1 < 0) and (n1 != 0)):
    print("O número informado é par e negativo!")
elif (n1 % 2 == 1) and ((n1 > 0) and (n1 != 0)):
    print("O número informado é ímpar e positivo!")
elif (n1 % 2 == 1) and ((n1 < 0) and (n1 != 0)):
    print("O número informado é ímpar e negativo!")
else:
    print("O número informado é par e neutro!")
