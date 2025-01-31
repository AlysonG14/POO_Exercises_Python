
'''
Challenge -  Implemente um sistema de gerenciamento de eventos, como um software para 
planejar e organizar eventos corporativos, casamentos, festas, etc. O sistema deve gerenciar o 
agendamento de eventos, as tarefas associadas a cada evento, os fornecedores e a 
distribuição de responsabilidades.
'''
import calendar
from datetime import datetime

class Evento:
    def __init__(self, data, hora, local, descrição):
        self.data = datetime.strptime(data, "%d/%m/%Y")
        self.hora = hora
        self.local = local
        self.descrição = descrição
        self.tarefas = []
        self.convidados = []
        self.pagamentos = []

    def adicionar_tarefas(self, tarefa):
        self.tarefas.append(tarefa)

    def adicionar_convidado(self, convidado):
        self.convidados.append(convidado)

    def registrar_pagamentos(self, pagamento):
        self.pagamentos.append(pagamento)

    def visualizar_evento(self):
        return f"{self.descrição} em {self.local} na data {self.data.strftime('%d/%m/%Y')}"
        
class Tarefa:
    def __init__(self, descricao, prazo, responsavel):
        self.descricao = descricao
        self.prazo = prazo
        self.responsavel = responsavel
        self.status = 'Pendente'

    def concluir_tarefa(self):
        self.status = 'Concluída'

    def atrasar_tarefa(self):
        self.status = 'Atrasada'

    def visualizar_tarefa(self):
        return f'Tarefa: {self.descricao} - Prazo: {self.prazo} - Status: {self.status} - Responsável: {self.responsavel.nome}'

class Responsável:
    def __init__(self, nome, carga):
        self.nome = nome
        self.carga = carga

    def visualizar_responsavel(self):
        return f"{self.nome} ({self.carga})"

class Convidado:
    def __init__(self, nome, presenca):
        self.nome = nome
        self.presenca = presenca

    def confirmar_presenca(self):
        self.presenca = True

    def visualizar_convidado(self):
        return '{} - Presença Confirmada: {}'.format(self.nome, self.presenca)
    
class Pagamento:
    def __init__(self, valor, data_pagamento, metodo):
        self.valor = valor
        self.data_pagamento = datetime.strptime(data_pagamento, "%d/%m/%Y")
        self.metodo = metodo
        self.status = 'Pago'

    def verificar_status(self, status):
        self.status = status

    def visualizar_pagamento(self):
        return "Pagamento R${:.2f} realizado em {} via {} - Status: {}".format(self.valor, self.data_pagamento.strftime("%d/%m/%Y"), self.metodo, self.status)

responsavel = Responsável('Alyson', 'Desenvolvedor Front End')
responsavel1 = Responsável('Rafael', 'Auxiliar Administrativo')
responsavel2 = Responsável('Renan', 'Repositor de Frios')

tarefa = Tarefa('Construir um Website de Lanches', '12/02/2026', responsavel)
tarefa1 = Tarefa('Chegar uma lista pelos dados gráficos','10/08/2025', responsavel1)
tarefa2 = Tarefa('Fazer uma montagem de palete', '05/02/2025', responsavel2)

evento = Evento('01/02/2025', '14:00', 'São Sebastião', 'Festa de Aniversário')

evento.adicionar_tarefas(tarefa)
evento.adicionar_tarefas(tarefa1)
evento.adicionar_tarefas(tarefa2)

convidado = Convidado('Gabriel Araújo', True)
convidado1 = Convidado('Lucas da Silva', False)

evento.adicionar_convidado(convidado)
evento.adicionar_convidado(convidado1)

pagamento = Pagamento(50.00, '02/02/2025', 'Dinheiro ou PIX')
evento.registrar_pagamentos(pagamento)

print(evento.visualizar_evento())
for tarefa in evento.tarefas:
    print(tarefa.visualizar_tarefa())
for convidado in evento.convidados:
    print(convidado.visualizar_convidado())
for pagamento in evento.pagamentos:
    print(pagamento.visualizar_pagamento())
