'''
Exercise 20 - Implemente um jogo de tabuleiro em que cada peça (peões, torres, etc.) seja representada por uma classe, com regras específicas de movimento e captura. No caso do xadrez, adicione a regra de roque, en passant, promoção de peões e xeque-mate.
'''

class Peca:
    def __init__(self, xadrez):
        self.xadrez = xadrez

    def movimentos(self, posicao):
        pass

class Peao(Peca):
    def __init__(self, xadrez):
        super().__init__(xadrez)

    def movimentos(self, posicao):
        pass

    def capturar(self, posicao):
        pass

    def promover(self):
        pass

class Torre(Peca):
    def __init__(self, xadrez):
        super().__init__(xadrez)

    def movimentos(self, posicao):
        pass

class Cavalo(Peca):
    def __init__(self, xadrez):
        super().__init__(xadrez)

    def movimentos(self, posicao):
        pass

class Bispo(Peca):
    def __init__(self, xadrez):
        super().__init__(xadrez)

    def movimentos(self, posicao):
        pass

class Rainha(Peca):
    def __init__(self, xadrez):
        super().__init__(xadrez)

    def movimentos(self, posicao):
        pass

class Rei(Peca):
    def __init__(self, xadrez):
        super().__init__(xadrez)

    def movimentos(self, posicao):
        pass

    def roque(self, posicao):
        pass

class Xadrez:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro
        self.jogo_em_andamento = True
    
    def criar_tabuleiro(self):
        tabuleiro = [[None for _ in range(8)]for _ in range(8)]

        tabuleiro[0] = [Torre('branca'), Cavalo('branca'), Bispo('branca'), Rainha('branca'), Rei('branca'), Bispo('branca'), Cavalo('branca'), Torre('branca')]
        tabuleiro[1] = [Peao('branco')for _ in range(8)]   
        tabuleiro[7] = [Torre('preta'), Cavalo('preta'), Bispo('preta'), Rainha('preta'), Rei('preta'), Bispo('preta'), Cavalo('preta'), Torre('preta')]
        tabuleiro[6] = [Peao('preto')for _ in range(8)]

        return tabuleiro
    
    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print(' '.join([str(peca.__class__.__name__[0])if peca else '.' for peca in linha]))

    def mover_peca(self, origem, destino):
        peca = self.tabuleiro[origem[0]][destino[1]]
        if peca and peca.movimentos(destino):

            self.tabuleiro[destino[0]][destino[1]] = peca
            self.tabuleiro[origem[0]][origem[1]] = None
            print('Peça movida de {} para {}'.format(origem, destino))
        else:
            print('Movimento Inválido')

    def verificar_checage(self):
        pass

    def verificar_mate(self):
        pass

    def realizar_roque(self, origem, destino):
        rei = self.tabuleiro[origem[0]][origem[1]]
        if isinstance(rei, Rei):
            rei.roque(destino)

xadrez = Xadrez()
xadrez.imprimir_tabuleiro()
xadrez.mover_peca((1, 0), (2, 0))

