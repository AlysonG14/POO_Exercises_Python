'''''
Exercise 02 - 
'''''
class ContaBancária():
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo


class Depósito(ContaBancária):
    def __init__(self, numero_conta, nome_titular, saldo, depósitos):
        super().__init__(numero_conta, nome_titular, saldo)
        self.depósitos = depósitos

class Saque(ContaBancária):
    def __init__(self, numero_conta, nome_titular, saldo, depósitos, saques):
        super().__init__(numero_conta, nome_titular, saldo, depósitos)
        self.saques = saques

ContaBancária('Número da Conta: 98569985\n', 'Nome Titular: Marcelo da Silva\n', 'Saldo: 2.000,00R$\n')

