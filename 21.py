'''
Exercise 21 - Construa uma aplicação de e-commerce onde produtos, clientes e pedidos são objetos. Adicione funcionalidades como carrinho de compras, desconto, cálculo de frete, histórico de compras e recomendação de produtos com base nas compras anteriores.
'''

class Ecommerce:
    def __init__(self, desconto, frete):
        self.carrinho = {}
        self.desconto = desconto
        self.frete = frete
        self.histórico_compras = []

    def carrinho_de_compras(self, nome, preco, quantidade):
        if nome in self.carrinho:
            print('Produto: {}'.format(nome))
        else:
            self.carrinho[nome] = (preco, quantidade)
            print('- Produto: {}. Preço: {}. Quantidade: {}')
    
    def lista_produtos(self):
        if self.carrinho:
            print('Lista de Produtos Disponíveis: ')
        for nome, (preco, quantidade) in self.carrinho.items():
            print('- Nome: {}. Preco: {}. Quantidade: {}'.format(nome, preco, quantidade))
        else:
            print('')
