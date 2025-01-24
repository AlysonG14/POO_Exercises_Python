'''
Exercise 06 - Implemente uma classe chamada “Produto” que possua atributos para armazenar o nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor total em estoque e verificar se o produto está disponível.
'''

class Produto:
    def __init__ (self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def __str__(self):
        return ('Nome: {}\n'
                'Preço R$: {:.2f}\n'
                'Quantidade: {}'.format(self.nome, self.preco, self.quantidade_estoque))

    def calcular_valor(self, Valor_Total):
        Valor_Total = self.preco * self.quantidade_estoque
        self.quantidade_estoque = True
        if self.quantidade_estoque >= 0:
            print('O Produto está disponível')
        else:
            print('O produto não está disponível')

