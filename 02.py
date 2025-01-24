'''
Exercise 02 -Implemente uma classe chamada “ContaBancária” que possua atributos para armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar depósitos e saques. 
'''

class ContaBancária():
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def __str__(self):
        return ('Número da Conta: {} \n'
                'Nome Títular: {} \n'
                'Saldo Atual: {:.2f}'.format(self.numero_conta, self.nome_titular, self.saldo))
                
    def calcular_depósito(self, valor):
            if valor > 0:
                self.saldo += valor
                print('O valor que você vai depositar é R$: {:.2f}'.format((valor)))
            else:
                print('Valor Inválido! Digite um valor maior que o zero!')
        
       
    def realizar_saques(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print('O valor que você vai realizar o saque é: {:.2f}'.format((valor)))
        elif valor > self.saldo:
            print('Saldo Insuficiente')
        else:
            print('Valor Inválido! Digite um valor maior que o zero')


    
Pessoa = ContaBancária(numero_conta=8542684, nome_titular='Marcelo da Silva', saldo=2.800)

print(Pessoa)

Pessoa.calcular_depósito(250)
Pessoa.realizar_saques(500)

print(Pessoa)


        
        