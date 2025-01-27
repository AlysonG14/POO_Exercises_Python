'''
Exericse 11 - Implemente uma classe chamada “Banco” que represente uma instituição financeira.
Essa classe deve conter métodos para cadastrar clientes, abrir contas bancárias e
realizar operações como saques, depósitos e transferências.
'''


class Banco:
    def __init__(self, saldo_inicial= 0):
        self.cadastroCliente = []
        self.ContasBancárias = saldo_inicial

    def __str__(self):
        return ('Clientes Cadastrados: {}\n'
                'Saldo do Banco: R$ {:.2f}'.format(self.cadastroCliente, self.ContasBancárias))
    
    def cadastro(self, nome):
        self.cadastroCliente.append(nome)
        print('Cliente: {} cadastro com sucesso!'.format(self.cadastroCliente))

    def listar_clientes(self):
        if self.cadastroCliente:
            print('Clientes cadastrados: ')
            for i, cliente in enumerate(self.cadastroCliente, start=1):
                print(f'{i}. {cliente}')
        else:
            print('Nenhum cliente cadastrado.')

    def realizar_saques(self, valor):
        if valor <= self.ContasBancárias:
            self.ContasBancárias -= valor
            print('Você sacou: R${:.2f}. Saldo atual: {:.2f}'.format(valor, self.ContasBancárias))
        else:
            print('Saldo Insuficiente')
    
    def fazer_depósitos(self, valor):
        if valor > 0:
            self.ContasBancárias += valor
            print('Você depositou: R${:.2f}. Saldo atual: R$ {:.2f}'.format(valor, self.ContasBancárias))
        else:
            print('Saldo Insuficiente')

    def transferências(self, valor):
        if valor <= self.ContasBancárias:
            self.ContasBancárias -= valor
            print('Você transferiu: R$ {:.2f}. Saldo atual: R$ {:.2f}'.format(valor, self.ContasBancárias))
        else:
            print('Saldo Insuficiente')

banco = Banco(saldo_inicial=2800)


for i in range(5):
    nome = input('Digite o nome do cliente: {} '.format(i + 1))
    banco.cadastro(nome)

banco.listar_clientes()
banco.realizar_saques(200)
banco.fazer_depósitos(500)
banco.transferências(800)        

print('\nEstado atual do Banco:')
print(banco)


