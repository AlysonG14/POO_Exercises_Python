class Produto:
    def __init__(self, nome, preco_de_compra, preco_de_venda, quantidade):
        self.nome = nome
        self.preco_de_compra = preco_de_compra
        self.preco_de_venda = preco_de_venda
        self.quantidade = quantidade

    def atualizar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f'Estoque atualizado para o produto {self.nome}: {self.quantidade} unidades.')

    def __str__(self):
        return f'{self.nome} - Compra: R${self.preco_de_compra:.2f}, Venda: R${self.preco_de_venda:.2f}, Estoque: {self.quantidade} unidades'


class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f'Produto {produto.nome} adicionado à categoria {self.nome}.')

    def listar_produtos(self):
        print(f'Produtos da categoria {self.nome}:')
        for produto in self.produtos:
            print(produto)


class Fornecedor:
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato

    def __str__(self):
        return f'{self.nome} - Contato: {self.contato}'


class Compra:
    def __init__(self, produto, fornecedor, quantidade, preco_de_compra):
        self.produto = produto
        self.fornecedor = fornecedor
        self.quantidade = quantidade
        self.preco_de_compra = preco_de_compra

    def realizar_compra(self):
        self.produto.atualizar_estoque(self.quantidade)
        print(f'Compra realizada: {self.quantidade} unidades de {self.produto.nome} do fornecedor {self.fornecedor.nome} por R${self.preco_de_compra:.2f} cada.')


class Venda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def realizar_venda(self):
        if self.produto.quantidade >= self.quantidade:
            self.produto.atualizar_estoque(-self.quantidade)
            valor_total = self.quantidade * self.produto.preco_de_venda
            print(f'Venda realizada: {self.quantidade} unidades de {self.produto.nome} por R${valor_total:.2f}.')
        else:
            print(f'Erro: Estoque insuficiente para realizar a venda de {self.quantidade} unidades de {self.produto.nome}.')



produto1 = Produto("Camiseta", 20.00, 50.00, 150)
produto2 = Produto("Shorts", 100.00, 89.99, 80)

categoria = Categoria("Roupas e Calçados")
categoria.adicionar_produto(produto1)
categoria.adicionar_produto(produto2)

fornecedor = Fornecedor("Fornecedor A", "contato@fornecedora.com")

compra1 = Compra(produto1, fornecedor, 200, 18.00)
compra1.realizar_compra()

venda1 = Venda(produto1, 50)
venda1.realizar_venda()

categoria.listar_produtos()
