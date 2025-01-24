'''
Exercise 04 - Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado).
'''


class Aluno:
    def __init__(self, nome, matrícula, notas):
        self.nome = nome
        self.matrícula = matrícula
        self.notas = notas

    def __str__(self):
        print('Nome: {} \n'
              'Matrícula: {}\n'
              'Notas em Geral: {}'.format(self.nome, self.matrícula, self.nome))

    def media_notas(self):
        nota1 = int(input("Digite a primeira nota: "))
        nota2 = int(input("Digite a segunda nota: "))
        nota3 = int(input("Digite a terceira nota: "))
        nota4 = int(input("Digite a quarta nota: "))
        self.notas = (nota1 + nota2 + nota3 + nota4) / 4
        print('A média das notas do aluno é: {}'.format(self.notas))
        return self.notas

    def verificar(self):
        if self.notas >= 6:
            print('Situação: APROVADO')
        else:
            print('Situação: REPROVADO')

resultado = Aluno(nome='Caique', matrícula= 28009, notas= 0)

resultado.media_notas()
resultado.verificar()

