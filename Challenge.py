'''
Challenge - Implemente um sistema de gerenciamento de eventos, como um software para planejar e organizar eventos corporativos, casamentos, festas, etc. O sistema deve gerenciar o agendamento de eventos, as tarefas associadas a cada evento, os fornecedores e a distribuição de responsabilidades.
'''

import calendar
from datetime import datetime

class Evento:
    def __init__(self, data, hora, local, descrição):
        self.data = data
        self.hora = hora
        self.local = local
        self.descrição = descrição
    
class Tarefa:
    def __init__(self, pendente, concluída, atrasada):
        self.pendente = pendente
        self.concluída = concluída
        self.atrasda = atrasada

class Responsável:
    def __init__(self, )
        
