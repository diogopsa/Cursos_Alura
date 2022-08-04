import forca
import adivinhacao
def escolhe_jogos():  
    print("*************************************")
    print("Escolha o seu jogo! [1] forca ou [2] adivinhacao?")
    print("*************************************")
    jogo = int(input("Qual jogo voce deseja jogar? "))
    if jogo ==1:
        print("O jogo escolhido foi forca")
        forca.jogar()()
    elif jogo ==2:
        print("O jogo escolhido foi adivinhacao")
        adivinhacao.jogar()
    else:
        print("Você deve escolher 1 para jogar forca ou 2 para jogar adivinhacao!")
if __name__ == "__main__":
    escolhe_jogos()