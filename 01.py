'''
Exercise 01 - Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e
métodos para calcular a área e o perímetro do círculo.
'''

class Círculo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_perímetro(self):
        self.raio = 5
        perímetro = 2 * (3.14) * self.raio
        print('Para calcular a área do perímetro dentro do círculo, é: {}'.format(perímetro))

class Perímetro(Círculo):
    def __init__(self, raio, perímetro):
        super().__init__(raio)
        self.perímetro = perímetro

    def calcular_area(self):  
        self.perímetro = 2
        área = (3.14) * self.perímetro ** 2
        print('E a área de um círculo de raio é dada por: {}'.format(área))

class Area(Círculo):
    def __init__(self, raio, perímetro, area):
        super().__init__(raio, perímetro)
        self.area = area











