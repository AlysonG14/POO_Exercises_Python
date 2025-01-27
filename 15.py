'''
Exercise 15 - Implemente uma classe chamada “JogoCartas” que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
'''

import random

class JogoCartas:
    def __init__(self):
        self.baralho = [str(num) for num in range(1, 10)] * 4 + ["Bloqueio", "Inverter", "Mais2"] * 4
        self.jogadores = []
        self.maos = {}

    def embaralhar_cartas(self):
        random.shuffle(self.baralho)
        print("Cartas embaralhadas!")

    def adicionar_jogadores(self, nomes):
        self.jogadores = nomes
        print(f"Jogadores adicionados: {', '.join(nomes)}")

    def distribuir_cartas(self, num_cartas=7):
        if not self.jogadores:
            print("Nenhum jogador cadastrado!")
            return

        self.maos = {jogador: [] for jogador in self.jogadores}
        for _ in range(num_cartas):
            for jogador in self.jogadores:
                if self.baralho:
                    self.maos[jogador].append(self.baralho.pop(0))  
                else:
                    print("O baralho acabou!")
                    break
        print("Cartas distribuídas aos jogadores!")

    def exibir_maos(self):
        for jogador, cartas in self.maos.items():
            print(f"{jogador}: {', '.join(cartas)}")

    def jogar_carta(self, jogador, carta):
        if jogador not in self.jogadores:
            print(f"Jogador {jogador} não encontrado!")
            return

        if carta not in self.maos[jogador]:
            print(f"Jogador {jogador} não tem a carta '{carta}'!")
            return

        self.maos[jogador].remove(carta)
        print(f"Jogador {jogador} jogou a carta '{carta}'.")

    def verificar_vencedor(self):
        for jogador, cartas in self.maos.items():
            if not cartas:  
                print(f"Jogador {jogador} venceu!")
                return jogador
        return None


jogo = JogoCartas()

jogo.adicionar_jogadores(["Alice", "Bob", "Carlos"])

jogo.embaralhar_cartas()

jogo.distribuir_cartas()

jogo.exibir_maos()

jogo.jogar_carta("Alice", "3")

jogo.exibir_maos()

jogo.verificar_vencedor()
        

     
