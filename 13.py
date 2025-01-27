'''
Exercise 13 - Implemente uma classe chamada “Agenda” que represente uma agenda telefônica.
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por
contatos a partir de um nome ou número de telefone.
'''

class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar(self, nome, numero):
        if not nome.strip():
            print('O nome não pode estar vazio!')
            return
        if not str(numero).isdigit():
            print('O número deve conter dígitos.')
            return
        if nome in self.contatos:
            print('Contato: {} já existe na agenda'.format(nome))
        else:
            self.contatos[nome] = str(numero)
            print('Contato: {} adicionado com sucesso!'.format(nome))

    def editar_contato(self, nome, novo_numero):
        if nome in self.contatos:
            self.contatos[nome] = novo_numero
            print(f'Contato atualizado: {nome} para o número: {novo_numero}')
        else:
            print(f'Contato: {nome} não encontrado')

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print('Contato: {} removido com sucesso'.format(nome))
        else:
            print('Contato: {} não encontrado!'.format(nome))

    def buscar_contato(self, termo):
        termo = str(termo)
        resultados = [
            f'{nome}: {numero}'
            for nome, numero in self.contatos.items()
            if termo.lower() in nome.lower() or termo in str(numero)
        ]
        if resultados:
            print('Resultados da Busca: ')
            for resultado in resultados:
                print(f'- {resultado}')
        else:
            print('Nenhum contato encontrado')

    def listar_contato(self):
        if self.contatos:
            print('Contatos na Agenda: ')
            for nome, numero in self.contatos.items():
                print(f'- Nome: {nome}, Número: {numero}')
        else:
            print('Nenhum contato na agenda!')

agenda = Agenda()

agenda.adicionar('Marcelo', 99261178)
agenda.adicionar('Marcela', 99261145)
agenda.adicionar('Murilo', 99261132)


agenda.listar_contato()

agenda.editar_contato('Murilo', 9923458)

agenda.buscar_contato('Marcela')
agenda.buscar_contato('2611')

agenda.remover_contato('Murilo')

agenda.listar_contato()


    

    
