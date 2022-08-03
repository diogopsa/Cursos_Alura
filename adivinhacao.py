#joguinho para acertar o número
print("*************************************")
print("Bem vindo ao jogo!")
print("*************************************")
numero_secreto = 42
chute = int(input("Digite o seu chute: "))
if (numero_secreto == chute):
    print("Parabéns!! Você acertou!")
else:
    print("Que pena, não foi dessa vez! Você errou!")
print("Fim do jogo")