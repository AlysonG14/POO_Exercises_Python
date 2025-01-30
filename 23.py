'''
Exercise 23 - Crie um sistema de gerenciamento de tarefas onde você tem tarefas com prioridades, datas de vencimento, status (pendente, em andamento, concluída) e categorias. Implemente funcionalidades de criar, editar, listar e excluir tarefas, além de filtros por status e prioridade.
'''

import heapq
import calendar
from datetime import datetime

class Gerenciamento:
    def __init__(self):
        self.fila_de_tarefas = []

    def adicionar_tarefa(self, descricao, prioridade, categoria, status, data_vencimento):
        tarefa = {
            'descricao': descricao,
            'prioridade': prioridade,
            'categoria': categoria,
            'status': status,
            'data_vencimento': data_vencimento
        }
        heapq.heappush(self.fila_de_tarefas, (prioridade, tarefa))

    def obter_tarefas(self):
        tarefas = []
        while self.fila_de_tarefas:
            prioridade, tarefa = heapq.heappop(self.fila_de_tarefas)
            tarefas.append(tarefa)
        return tarefas

    def listar_tarefas(self):
        if not self.fila_de_tarefas:
            print("Nenhuma tarefa encontrada.")
        else:
            for prioridade, tarefa in self.fila_de_tarefas:
                print(f"Descrição: {tarefa['descricao']}, Prioridade: {tarefa['prioridade']}, "
                      f"Categoria: {tarefa['categoria']}, Status: {tarefa['status']}, "
                      f"Data de Vencimento: {tarefa['data_vencimento']}")

    def excluir_tarefa(self, descricao):
        self.fila_de_tarefas = [tarefa for tarefa in self.fila_de_tarefas if tarefa[1]['descricao'] != descricao]
        print(f"Tarefa '{descricao}' excluída com sucesso!")

    def exibir_calendario(self, ano, mes):
        print(calendar.month(ano, mes))

    def filtrar_por_status(self, status):
        tarefas_filtradas = [tarefa for _, tarefa in self.fila_de_tarefas if tarefa['status'] == status]
        return tarefas_filtradas

    def filtrar_por_prioridade(self, prioridade):
        tarefas_filtradas = [tarefa for _, tarefa in self.fila_de_tarefas if tarefa['prioridade'] == prioridade]
        return tarefas_filtradas

    def verificar_data_vencimento(self):
        data_atual = datetime.now()
        for _, tarefa in self.fila_de_tarefas:
            data_vencimento = datetime.strptime(tarefa['data_vencimento'], "%d/%m/%Y")
            if data_vencimento < data_atual:
                print(f"Tarefa '{tarefa['descricao']}' está vencida!")
            else:
                print(f"Tarefa '{tarefa['descricao']}' não está vencida.")

    def editar_tarefa(self, descricao, nova_descricao=None, nova_prioridade=None, nova_categoria=None, novo_status=None, nova_data=None):
        for prioridade, tarefa in self.fila_de_tarefas:
            if tarefa['descricao'] == descricao:
                if nova_descricao:
                    tarefa['descricao'] = nova_descricao
                if nova_prioridade:
                    tarefa['prioridade'] = nova_prioridade
                if nova_categoria:
                    tarefa['categoria'] = nova_categoria
                if novo_status:
                    tarefa['status'] = novo_status
                if nova_data:
                    tarefa['data_vencimento'] = nova_data
                print(f"Tarefa '{descricao}' foi editada com sucesso!")
                break

gerenciamento = Gerenciamento()
gerenciamento.adicionar_tarefa("Visitar o Chefe", "URGENTE", "Trabalho", "Pendente", "10/02/2025")
gerenciamento.adicionar_tarefa("Terminar o Projeto Integrador", "Não Urgente", "Estudo", "Em andamento", "25/12/2025")
gerenciamento.adicionar_tarefa("Viajar para Amazônia", "URGENTE", "Lazer", "Pendente", "01/03/2025")

gerenciamento.listar_tarefas()

pendentes = gerenciamento.filtrar_por_status("Pendente")
print("Tarefas pendentes:", pendentes)

gerenciamento.exibir_calendario(2025, 1)

gerenciamento.verificar_data_vencimento()

gerenciamento.editar_tarefa("Viajar para Amazônia", novo_status="Concluído", nova_data="01/02/2025")

gerenciamento.excluir_tarefa("Terminar o Projeto Integrador")
