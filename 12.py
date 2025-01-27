'''
Exercise 12 - Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho de
compras, aplicar descontos e calcular o valor total da compra.
'''

class LojaVirtual:
    def __init__(self):
        self.cadastrarProduto = {}
        self.carrinhodeCompras = []
        self.Valor_Total = 0

    def __str__(self):
        return ('Produtos no Carrinho: {}\n'
                'Valor Total: R$ {:.2f}'.format(self.carrinhodeCompras, self.Valor_Total))

    def cadastro(self, nome, preco):
        self.cadastrarProduto[nome] = preco
        print('Produto: {} cadastrado com sucesso. Preço: R${:.2f}'.format(self.cadastrarProduto, preco))
    
    def listar_produtos(self):
        if self.cadastrarProduto:
            print('Produtos Cadastrados: ')
            for nome, preco in self.cadastrarProduto.items():
                print('- {}: R$ {:.2f}'.format(nome, preco))
        else:
            print('Nenhum produto cadastrado.')

    def carrinho(self, nome):
        if nome in self.cadastrarProduto:
            self.carrinhodeCompras.append(nome)
            self.Valor_Total += self.cadastrarProduto[nome]
            print('Produto: {} adicionado ao carrinho'.format(nome))
        else:
            print('Produto: {} não encontrado'.format(nome))
                

    def desconto(self, desconto):
        if desconto > 0 and desconto <= self.Valor_Total:
            self.Valor_Total -= desconto
            print('Desconto de R$ {} aplicado com sucesso!'.format(desconto))
        else:
            print('Desconto Inválido!')

    def calcular_valor_total(self):
        print('Valor total da compra: R$ {:.2f}'.format(self.Valor_Total))

loja = LojaVirtual()

loja.cadastro('Tênis', 40.89)
loja.cadastro('Camisa', 20.00)
loja.cadastro('Calça', 90.00)

loja.listar_produtos()

loja.carrinho('Tênis')
loja.carrinho('Camisa')
loja.carrinho('Calça')

loja.desconto(20)

loja.calcular_valor_total()

print('\nEstado final: ')
print(loja)

        



    