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

    def calcular_valor(self):
        Valor_Total = self.quantidade_estoque * self.preco

        if self.quantidade_estoque > 0:
            print('Produto Disponível, o valor total é: R${:.2f}'.format(Valor_Total))
        else:
            print('Produto Indisponível')

resultado = Produto('Arroz Integral', 400, 300)
print(resultado)

resultado.calcular_valor()



