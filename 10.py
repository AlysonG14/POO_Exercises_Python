'''
Exercise 10 - Implemente uma classe chamada “Livro” com atributos para armazenar o título, o 
autor e o número de páginas do livro. Adicione métodos para emprestar o livro, 
devolvê-lo e verificar se está disponível.
'''

class Livro:
    def __init__(self, título, autor, número_páginas_livro):
        self.título = título
        self.autor = autor
        self.número_páginas_livro = número_páginas_livro
        self.disponível = True

    def __str__(self):
        return ('Título: {}\n'
                'Autor: {} \n'
                'Número de Páginas: {}'.format(self.título, self.autor, self.número_páginas_livro))
    
    def emprestar(self):
        if self.disponível:
            while True:
                emprestar = input('Você me emprestaria esse livro: {} (sim/não)? '.format(self.título))
                if emprestar == 'sim':
                    self.disponível = False
                    print('Sim? Ótimo, muito, obrigado')
                    break
                elif emprestar == 'não':
                    print('Tudo bem, talvez outro livro seja melhor!')
                    break
                else:
                    print('Digitação Inválida! Por favor, inserir sim ou não.')
        else:
            print("O livro: {} não está disponível nesse momento".format(self.título))


    def devolver(self):
        if not self.disponível:
            while True:
                devoluçao = input('Deseja fazer uma devolução desse livro: {} (sim/não)? '.format(self.título))
                if devoluçao == 'sim':
                    self.disponível = True
                    print('Sim? Obrigado, volte sempre!')
                    break
                elif devoluçao == 'não':
                    print('Não? Então tá bom, volte sempre!')
                    break
                else:
                    print('Digitação Inválida! Por favor, inserir sim ou não.')
        else:
            print("O livro: {} não está disponível nesse momento".format(self.título))

    def verificação(self):
        if self.disponível:
            print('O livro: {} está disponível'.format(self.título))
        else:
            print('O livro: {} não está disponível'.format(self.título))


resultado = Livro('A Revolução dos Bichos', 'George Orwell', 152)
print(resultado)

resultado.verificação()
resultado.emprestar()
resultado.verificação()
resultado.devolver()
resultado.verificação()
