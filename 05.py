'''
Exercise 05 - Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, considerando descontos de impostos e benefícios.
'''

class Funcionário: 
    def __init__(self, nome, salário, cargo_funcionário):
        self.nome = nome
        self.salário = salário
        self.cargo_funcionário = cargo_funcionário

    def __str__(self):
        return (f'Nome: {self.nome} \n'
                f'Salário {self.salário}\n'
                f'Cargo do Funcionário: {self.cargo_funcionário}')
    
    def calcular_salário_líquido(self, descontos_impostos):
        if descontos_impostos >= 0 and self.salário - 2 * (0.075):
            self.salário -= descontos_impostos
            print('Você descontou os impostos no valor de {}, seu salário líquido atual é: R$ {:.3f}'.format(descontos_impostos, self.salário))
        else: 
            print('Número Inválido!')
            return self.salário

    def calcular_salário_líquido1(self, descontos_beneficios):
        if descontos_beneficios >= 0:
            self.salário -= descontos_beneficios
            print('Você descontou os benefícios no valor de {}, seu salário líquido atual é: R$ {:.3f}'.format(descontos_beneficios, self.salário))
        else:
            print('Número Inválido')
            return self.salário



pessoa = Funcionário('Alyson', 12500, 'Desenvolvedor Full-Stack')
pessoa.calcular_salário_líquido(200)
pessoa.calcular_salário_líquido1(500)
    

