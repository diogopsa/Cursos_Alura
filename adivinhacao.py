#joguinho para acertar o número
print("*************************************")
print("Bem vindo ao jogo!")
print("*************************************")
numero_secreto = 42
chute = int(input("Digite o seu chute: "))
acertou = chute == numero_secreto
maior = chute > numero_secreto
if (acertou):
    print("Parabéns!! Você acertou!")
else:
    if (maior):
        print("O número que você chutou é maior que o número secreto!!")
    else:
        print("O número que você chutou é menor que o número secreto!!")
    print("Que pena, não foi dessa vez! Você errou!")
print("Fim do jogo")
