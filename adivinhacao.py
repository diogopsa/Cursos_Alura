import random
print("*************************************")
print("Bem vindo ao jogo!")
print("*************************************")
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000
print("Qual o nivel de dificuldade?")
print("[1] facil, [2] medio ou [3] dificil?")
nivel = int(input("Digite o nivel de dificuldade: "))
if (nivel ==1):
    total_de_tentativas = 20
elif (nivel ==2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
for rodada in range (1,total_de_tentativas+1):
    print("Rodada {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu chute: "))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    if (chute < 1 or chute > 100):
        print("Voce deve entrar com um valor entre 1 e 100!!")
        continue
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    
    if (acertou):
        print("Parabens!! Voce acertou e fez {}!".format(pontos))
        break
    else:
        if (maior):
            print("O numero que voce chutou foi maior que o numero secreto!!")
        else:
            print("O numero que voce chutou foi menor que o numero secreto!!")
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = (pontos - pontos_perdidos)
print("Fim do jogo")
