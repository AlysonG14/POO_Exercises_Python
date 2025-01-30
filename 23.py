'''
Exercise 23 - Crie um sistema de gerenciamento de tarefas onde você tem tarefas com prioridades, datas de vencimento, status (pendente, em andamento, concluída) e categorias. Implemente funcionalidades de criar, editar, listar e excluir tarefas, além de filtros por status e prioridade.
'''

import heapq
import calendar
from datetime import datetime

class Gerenciamento:
    def __init__(self, descricao, data):
        self.prioridade = []
        self.descricao = descricao
        self.data = str(data)
        self.status = {}
        self.categorias = {}
        self.fila_de_tarefas = []

    def adicionar_tarefa(self, tarefa, prioridade):
        heapq.heappush(self.fila_de_tarefas, (prioridade, tarefa))

    def obter_tarefas(self):
        if self.fila_de_tarefas:
            return heapq.heappop(self.fila_de_tarefas)
        else:
            return None

    def exibir_calendario(self, mes, dia):
        print(calendar.month(mes, dia))

    def datas(self, dia, mes, ano):
        data_consulta  = '%d/%m/%Y'
        if self.data in data_consulta:
            print('Aqui está as datas:')
            if ano (mes, dia) in self.data_vencimento:
                print('{}/{}/{}'.format(dia, mes, ano))
            else:
                print('Nenhuma data encontrada')

    def data_de_vencimento(self):
        data_vencimento = datetime(12, 20, 2026)
        data_atual = datetime.now()
        if data_vencimento > data_atual:
            print('Data de Vencimento: Concluído')
        elif data_vencimento < data_atual:
            print('Data de Vencimento: Não Chegou')
        else:
            print('Data Inválido')
        
gerenciamento = Gerenciamento('Descrição: Tarefas para concluir: ', 2005)
gerenciamento.adicionar_tarefa('Visitar o Chefe', 'URGENTE')
gerenciamento.adicionar_tarefa('Terminar o Projeto Integrador', 'Não Urgente')
gerenciamento.adicionar_tarefa('Viajar para Amâzonia', 'URGENTE')

gerenciamento.obter_tarefas()

gerenciamento.exibir_calendario(8, 12)

gerenciamento.datas(8, 12, 2005)

gerenciamento.data_de_vencimento()


            

    

     
