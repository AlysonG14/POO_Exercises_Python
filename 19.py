'''
19. Implemente uma classe chamada “JogoAdivinhacao” que represente um jogo de adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça palpites e informar se o palpite está correto, informando se é maior ou menor que o número gerado.
'''

import random

class JogoAdivinhacao:
    def __init__(self): 
        self.aleatorio = random.randint(1, 20)
        self.chances = 6
        self.ganhou = False

    def jogar(self):
        print('Bem-vindo ao jogo de adivinhação: ')
        print(f'Você tem {self.chances} tentativas para adivinhar o jogo!')
        while self.chances > 0 and not self.ganhou:
            palpite = int(input("Digite o seu palpite: "))

            if palpite == self.aleatorio:
                self.ganhou = True
                print('Parabéns, você adivinhou o número, o número que eu pensei é o {}'.format(self.aleatorio))
            elif palpite < self.aleatorio:
                self.chances -= 1
                print('O número é maior. Você tem mais {} chances'.format(self.chances))
            else:
                self.chances -= 1
                print('O númmero é menor. Você tem mais {} chances'.format(self.chances))

            if self.chances == 0 and not self.ganhou:
                print('Você perdeu o jogo, o número que eu adivinhei é o número: {}'.format(self.aleatorio)) 
                break


game = JogoAdivinhacao()
game.jogar()
