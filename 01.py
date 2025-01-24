'''
Exercise 01 - Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e
métodos para calcular a área e o perímetro do círculo.
'''

class Círculo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_perímetro(self):
        self.perímetro = 2 * (3.14) * self.raio
        print('A área do perímetro dentro do círculo, é: {}'.format(self.perímetro))

    def calcular_area(self):  
        self.área = (3.14) * self.raio ** 2
        print('A área de um círculo de raio é dada por: {}'.format(self.área))

círculo = Círculo(5)
círculo.calcular_perímetro()
círculo.calcular_area()


    










