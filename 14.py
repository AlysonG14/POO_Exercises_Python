'''
Exercise 14 - Crie uma classe chamada “MáquinaDeVendas” que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.
'''

class MáquinaDeVendas:
    def __init__(self):
        self.CadastroProduto = {}

    def __str__(self):
        return ('Produtos Cadastrados: {}'.format(self.CadastroProduto))

    def cadastro(self, nome, preco, quantidade):
        if nome in self.CadastroProduto:
            print('O produto {} já está cadastrado.'.format(nome))
        else:
            self.CadastroProduto[nome] = (preco, quantidade)
            print('Produtos {} cadastrado com sucesso. Preço: {}. Estoque disponível: {}'.format(nome, preco, quantidade))

    def lista_produto(self):
        if self.CadastroProduto:
            print('Produtos Disponíveis: ')
            for nome, (preco, quantidade) in self.CadastroProduto.items():
                print('- Nome: {}. Preço: R$ {:.2f}. Estoque: {}'.format(nome, preco, quantidade))
        else:
            print('Nenhum produto cadastrado!')

    def selecionar_produto(self, nome):
        if nome in self.CadastroProduto:
            preco, quantidade = self.CadastroProduto[nome]
            if quantidade > 0:
                print('Produto: {} selecionado. Preço: {:.2f}'.format(nome, preco))
                return nome
            else:
                print('O produto {} está fora de estoque'.format(nome))
        else:
            print('O produto {} não foi encontrado'.format(nome))
        return nome

    def inserir_dinheiro(self, nome, valor):
        if nome in self.CadastroProduto:
            preco, quantidade = self.CadastroProduto[nome]
            if valor >= preco:
                troco = valor - preco
                self.CadastroProduto[nome] = (preco, quantidade - 1)
                print('Compra realizada com sucesso! Você pagou: {}. E o Troco: {}'.format(preco,troco))
            else:
                print('Dinheiro Insuficiente. O preço custa: {}'.format(preco))

máquina = MáquinaDeVendas()

máquina.cadastro('Leite', 20.00, 4)
máquina.cadastro('Água', 3.00, 10)
máquina.cadastro('Pão', 10.00, 8)

máquina.lista_produto()

máquina.selecionar_produto('Água')

máquina.inserir_dinheiro('Leite', 30.00)            
                

            


