'''
Exercise 08 - Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o 
modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a 
velocidade atual.
'''

class Carro:
    def __init__(self, marca, modelo, velocidade_atual):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual

    def __str__(self):
        return(f'Marca: {self.marca}\n'
               f'Modelo: {self.modelo}\n'
               f'Velocidade: {self.velocidade_atual} km/h')

    def calcular_acelerar(self, Variação_velocidade, Intervalo_tempo):
        aceleração = Variação_velocidade / Intervalo_tempo
        print('A aceleração do carro é: {} m/s'.format(aceleração))

        self.velocidade_atual += Variação_velocidade
        print('Nova velocidade após acelerar: {} km/h'.format(self.velocidade_atual))

    def calcular_frear(self, Variação_velocidade, Intervalo_tempo):
        frenagem = - Variação_velocidade / Intervalo_tempo
        print('A frenagem do carro é: {} m/s'.format(frenagem))

        self.velocidade_atual -= Variação_velocidade
        print('Nova velocidade após frear: {} km/h'.format(self.velocidade_atual))

resultado = Carro('Toyota', 'Corolla', 230)
print(resultado)

resultado.calcular_acelerar(20, 40)
resultado.calcular_frear(30, 30)
