'''
Exercise 20 - Implemente um jogo de tabuleiro em que cada peça (peões, torres, etc.) seja representada por uma classe, com regras específicas de movimento e captura. No caso do xadrez, adicione a regra de roque, en passant, promoção de peões e xeque-mate.
'''

class Peca:
    def __init__(self, xadrez, cor):
        self.xadrez = xadrez
        self.cor = cor

    def movimentos(self, posicao):
        pass

class Peao(Peca):
    def __init__(self, xadrez, cor):
        super().__init__(xadrez, cor)

    def movimentos(self, posicao):
        pass  # Movimentação de peão

class Torre(Peca):
    def __init__(self, xadrez, cor):
        super().__init__(xadrez, cor)

    def movimentos(self, posicao):
        movimentos_possiveis = []
        # Movimentos na vertical e horizontal
        for i in range(1, 8):
            # Movimento para baixo
            if posicao[0] + i < 8:  # Não ultrapassar o limite do tabuleiro
                movimentos_possiveis.append((posicao[0] + i, posicao[1]))
            # Movimento para cima
            if posicao[0] - i >= 0:  # Não ultrapassar o limite do tabuleiro
                movimentos_possiveis.append((posicao[0] - i, posicao[1]))
            # Movimento para a direita
            if posicao[1] + i < 8:  # Não ultrapassar o limite do tabuleiro
                movimentos_possiveis.append((posicao[0], posicao[1] + i))
            # Movimento para a esquerda
            if posicao[1] - i >= 0:  # Não ultrapassar o limite do tabuleiro
                movimentos_possiveis.append((posicao[0], posicao[1] - i))
        return movimentos_possiveis

class Cavalo(Peca):
    def __init__(self, xadrez, cor):
        super().__init__(xadrez, cor)

    def movimentos(self, posicao):
        pass

class Bispo(Peca):
    def __init__(self, xadrez, cor):
        super().__init__(xadrez, cor)

    def movimentos(self, posicao):
        pass

class Rainha(Peca):
    def __init__(self, xadrez, cor):
        super().__init__(xadrez, cor)

    def movimentos(self, posicao):
        pass

class Rei(Peca):
    def __init__(self, xadrez, cor):
        super().__init__(xadrez, cor)

    def movimentos(self, posicao):
        pass

    def roque(self, posicao):
        pass

class Xadrez:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()
        self.jogo_em_andamento = True
    
    def criar_tabuleiro(self):
        tabuleiro = [[None for _ in range(8)]for _ in range(8)]

        tabuleiro[0] = [Torre(self, 'branca'), Cavalo(self, 'branca'), Bispo(self, 'branca'), Rainha(self, 'branca'), Rei(self, 'branca'), Bispo(self, 'branca'), Cavalo(self, 'branca'), Torre(self, 'branca')]
        tabuleiro[1] = [Peao(self, 'branco') for _ in range(8)]   
        tabuleiro[7] = [Torre(self, 'preta'), Cavalo(self, 'preta'), Bispo(self, 'preta'), Rainha(self, 'preta'), Rei(self, 'preta'), Bispo(self, 'preta'), Cavalo(self, 'preta'), Torre(self, 'preta')]
        tabuleiro[6] = [Peao(self, 'preto') for _ in range(8)]

        return tabuleiro
    
    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print(' '.join([str(peca.__class__.__name__[0]) if peca else '.' for peca in linha]))

    def mover_peca(self, origem, destino):
        peca = self.tabuleiro[origem[0]][origem[1]]
        movimentos_validos = peca.movimentos(origem)
        if destino in movimentos_validos:
            # Verificar se o destino não está ocupado por uma peça da mesma cor
            destino_peca = self.tabuleiro[destino[0]][destino[1]]
            if destino_peca is None or destino_peca.cor != peca.cor:
                self.tabuleiro[destino[0]][destino[1]] = peca
                self.tabuleiro[origem[0]][origem[1]] = None
                print(f'Peça movida de {origem} para {destino}')
            else:
                print('Movimento inválido: Destino ocupado por peça da mesma cor')
        else:
            print('Movimento inválido')

    def verificar_checagem(self):
        pass

    def verificar_mate(self):
        pass

    def realizar_roque(self, origem, destino):
        rei = self.tabuleiro[origem[0]][origem[1]]
        if isinstance(rei, Rei):
            rei.roque(destino)


# Testando a funcionalidade
xadrez = Xadrez()
xadrez.imprimir_tabuleiro()
xadrez.mover_peca((1, 0), (2, 0))  # Move um peão
xadrez.mover_peca((0, 0), (3, 0))  # Tenta mover uma torre (exemplo)
