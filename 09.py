'''
Exercise 09 - Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a 
idade e o histórico de consultas de um paciente. Implemente métodos para adicionar 
uma nova consulta ao histórico e exibir as consultas realizadas.
'''

from datetime import datetime

class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.histórico_consultas_paciente = []
        self.contador = 0

    def __str__(self):
        return ('Nome: {}'
                'Idade: {}'
                'Histórico: {}'.format(self.nome, self.idade, self.histórico_consultas_paciente))


    def nova_consulta(self):
     consulta = ''
     while consulta not in ['sim', 'não']:
      consulta = input("Deseja marcar uma consulta: (sim/não)? ").lower()
     if consulta == 'sim':
          data_consulta = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
          self.histórico_consultas_paciente.append(data_consulta)
          print(f'Seja bem vindo, sua consulta foi registrada em {data_consulta}')
          self.contador += 1
     elif consulta == 'não':
           print('Desejo uma boa sorte, volte mais tarde!')
     else:
           print('Entrada inválida. Por favor, digite "sim" ou "não"')
    
    def historico_consulta(self):
        if self.histórico_consultas_paciente:
            print('O seu histórico de consultas é: {}'.format(self.contador))
            for consulta in self.histórico_consultas_paciente:
                print(consulta)
        else:
            print('Nenhum registro ainda')

    
resultado = Paciente('Alyson', 20)
resultado.nova_consulta()
resultado.historico_consulta()


          
