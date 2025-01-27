'''
Exercise 07 - Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do
triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua
área.
'''

import math

class Triângulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def verificação(self):
        return self.a > 0 and self.b > 0 and self.c > 0 and (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a)

    def calcular_Equilátero(self):
        if self.a == self.b == self.c and self.verificação():
            Área = (self.a ** 2 * math.sqrt(3)) / 4
            print(f'Triângulo Equilátero válido, sua área é: {Área}')
        else:
            print('Triângulo Equilátero inválido')

    def calcular_Isósceles(self, altura):
        if self.verificação() and (self.a == self.b or self.a == self.c or self.b == self.c):
            if altura > 0:  
                Área = (self.a * altura) / 2  
                print(f'Triângulo Isósceles válido, sua área é: {Área}')
            else:
                print('Altura inválida! A altura deve ser maior que 0.')
        else:
            print('Triângulo Isósceles inválido')

    def calcular_Escaleno(self):
        if self.verificação() and self.a != self.b and self.b != self.c and self.a != self.c:
            s = (self.a + self.b + self.c) / 2 
            Área = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            print(f'Triângulo Escaleno válido, sua área é: {Área}')
        else:
            print('Triângulo Escaleno Inválido')


calculo = Triângulo(12, 12, 12)
calculo.calcular_Equilátero()

calculo = Triângulo(20, 20, 40)
calculo.calcular_Isósceles(40)  


calculo = Triângulo(5, 8, 3)
calculo.calcular_Escaleno()