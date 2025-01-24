'''
Exercise 03 - Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e a altura. Implemente métodos para calcular a área e o perímetro do retângulo.
'''

class Retângulo:
    def __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calculando_area(self):
        Área = self.largura * self.altura
        print('A área do retângulo é: {}'.format(Área))

    def calculando_perímetro(self):
        Perímetro = 2 * (self.altura + self.largura)
        print('O perímetro do retângulo é: {}'.format(Perímetro))

resultado = Retângulo(2, 4)
resultado.calculando_area()
resultado.calculando_perímetro()

# Altura = (H)
# Largura = (B)
