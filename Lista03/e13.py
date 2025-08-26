'''Faça um algoritmo para entrar com o nome da capital do Brasil. Se a resposta estiver correta,
imprimir PARABÉNS, caso contrário, ERROU. (Considerar: BRASÍLIA ou Brasília)'''

capital = input("Digite o nome da capital do Brasil: ")
if capital == "BRASÍLIA" or capital == "Brasília":
    print("PARABÉNS")
else:
    print("ERROU")
