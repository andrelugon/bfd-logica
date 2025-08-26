'''Elaborar um algoritmo que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo. Supor
que os valores lidos são inteiros e positivos. Caso os valores formem um triângulo, calcular e
escrever o tipo de triângulo (escaleno, isósceles ou eqüilátero). Se não formam triângulo escrever
os valores lidos. Propriedade — O comprimentod e cada lado de um triânguloé menor do que a
soma dos comprimentos dos outros dois lados.
Definição 1 — Triângulo equilátero é o triângulo que tem os comprimentos dos três lados iguais.
Definição 2 — Triângulo isósceles é o triânguloq ue tem os comprimentosd e dois lados iguais.
Portanto, todo triângulo equilátero é também isósceles.
Definição 3 — Triângulo escaleno é o triângulo que tem os comprimentos dos três lados diferentes.'''

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print(f"{a}, {b}, {c} - O comprimento de cada lado de um triângulo é menor do que a
soma dos comprimentos dos outros dois lados")
