'''
Exercise 25 - Crie um jogo de combate onde personagens são objetos com atributos como saúde, força, defesa, e habilidades especiais. Implemente combate entre personagens, uso de itens (como poções de cura), e eventos de vitória ou derrota. O sistema pode incluir também níveis de experiência e evolução dos personagens.
'''

import random

class Personagem:
    def __init__(self, nome, saúde, força, defesa, habilidades_especiais=None):

        if habilidades_especiais is None:
            habilidades_especiais = []
        self.nome = nome
        self.saúde = saúde
        self.força = força
        self.defesa = defesa
        self.habilidades_especiais = habilidades_especiais
        self.experiencia = 0
        self.nivel = 1

    def atacar(self, outro_personagem):
        dano = self.força - outro_personagem.defesa
        if dano < 0:
            dano = 0
        outro_personagem.saúde -= dano
        print(f"{self.nome} atacou {outro_personagem.nome} causando {dano} de dano!")

    def usar_pocao(self):
        cura = 20
        self.saúde += cura
        print(f"{self.nome} usou uma poção e recuperou {cura} pontos de saúde!")

    def ganhar_experiencia(self, pontos):
        self.experiencia += pontos
        print(f"{self.nome} ganhou {pontos} pontos de experiência!")
        self.verificar_evolucao()

    def verificar_evolucao(self):
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            self.força += 5
            self.defesa += 3
            print(f"{self.nome} evoluiu para o nível {self.nivel}!")

    def esta_vivo(self):
        return self.saúde > 0

class Jogo:
    def __init__(self):
        self.personagens = []

    def adicionar_personagem(self, personagem):
        self.personagens.append(personagem)

    def batalha(self, personagem1, personagem2):
        print(f"Iniciando batalha entre {personagem1.nome} e {personagem2.nome}")
        while personagem1.esta_vivo() and personagem2.esta_vivo():
            personagem1.atacar(personagem2)
            if not personagem2.esta_vivo():
                print(f"{personagem2.nome} foi derrotado!")
                personagem1.ganhar_experiencia(50)
                break

            personagem2.atacar(personagem1)
            if not personagem1.esta_vivo():
                print(f"{personagem1.nome} foi derrotado!")
                personagem2.ganhar_experiencia(50)
                break

    def mostrar_status(self, personagem):
        print(f"{personagem.nome}: Saúde={personagem.saúde}, Força={personagem.força}, Defesa={personagem.defesa}, Nível={personagem.nivel}, Experiência={personagem.experiencia}")

if __name__ == "__main__":
    personagem1 = Personagem(nome="Batman", saúde=100, força=30, defesa=10)
    personagem2 = Personagem(nome="Coringa", saúde=80, força=40, defesa=5)

    jogo = Jogo()
    jogo.adicionar_personagem(personagem1)
    jogo.adicionar_personagem(personagem2)

    jogo.mostrar_status(personagem1)
    jogo.mostrar_status(personagem2)

    jogo.batalha(personagem1, personagem2)
    jogo.mostrar_status(personagem1)
    jogo.mostrar_status(personagem2)
