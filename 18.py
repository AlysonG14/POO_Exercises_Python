'''
Exercise 18 - Crie uma classe chamada “Calendario” que represente um calendário anual. Essa classe deve ter métodos para exibir o calendário de um determinado mês, verificar se uma data é feriado e calcular a diferença de dias entre duas datas.
'''
import calendar
from datetime import datetime

class Calendario:
    def __init__(self):
        self.feriados = [(1, 1), (25, 12), (8, 12)]
        self.calendario = {}
    
    def exibir_calendario(self, ano, mes):
        print(calendar.month(ano, mes))

    def verificar_calendario(self, dia, mes):
        if (dia, mes) in self.feriados:
            print(f'{dia}/{mes} é feriado')
        else:
            print(f'{dia}/{mes} não é feriado')
        
    def calcular_diferenca_dias(self, data1, data2):
        formato = "%d/%m/%Y"
        try:
            data1 = datetime.strptime(data1, formato)
            data2 = datetime.strptime(data2, formato)
            diferenca = abs((data2 - data1).days)
            print(f'A diferença entre {data1.strftime(formato)} e {data2.strftime(formato)} é de {diferenca} dias')
        except ValueError:
            print('Formato de data inválido. Use dd/mm/yyyy')




calendario = Calendario()
calendario.exibir_calendario(2025, 4)
calendario.verificar_calendario(21, 4)
calendario.calcular_diferenca_dias("15/08/2008", "25/12/2008")
calendario.calcular_diferenca_dias("10/01/2005", "31/01/2005")
