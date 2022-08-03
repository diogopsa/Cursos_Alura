print("*************************************")
print("Bem vindo ao jogo!")
print("*************************************")
numero_secreto = 42
rodada = 1
total_de_tentativas = 3
while rodada <= total_de_tentativas:
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute = int(input("Digite o seu chute: "))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    if (acertou):
        print("Parabens!! Voce acertou!")
    else:
        if (maior):
            print("O numero que voce chutou foi maior que o numero secreto!!")
        else:
            print("O numero que voce chutou foi menor que o numero secreto!!")
        print("Que pena, nao foi dessa vez! Voce errou!")
    rodada = rodada +1
print("Fim do jogo")
