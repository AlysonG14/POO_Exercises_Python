'''
Exercise 23 - Crie um sistema de gerenciamento de tarefas onde você tem tarefas com prioridades, datas de vencimento, status (pendente, em andamento, concluída) e categorias. Implemente funcionalidades de criar, editar, listar e excluir tarefas, além de filtros por status e prioridade.
'''

import heapq
from datetime import datetime

class Gerenciamento:
    def __init__(self, tarefa_prioridade, descricao, data_vencimento):
        self.prioridade = tarefa_prioridade
        self.descricao = descricao
        self.data_vencimento = data_vencimento
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

     
