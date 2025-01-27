'''
Exercise 17 - Implemente uma classe chamada “Biblioteca” que represente uma biblioteca virtual. Essa classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar a disponibilidade de um livro.
'''

class Biblioteca:
    def __init__(self):
        self.books = {}

    def cadastrar_livros(self, name_book):
        if name_book in self.books:
            print('O livro "{}" já está cadastrado na biblioteca!'.format(name_book))
        else:
            self.books[name_book] = {'disponível': True}
            print('O livro "{}" foi cadastrado com sucesso!'.format(name_book))

    def emprestar_livro(self, name_book):
        if name_book not in self.books:
            print(f'O livro "{name_book}" não existe na biblioteca!')
        elif self.books[name_book]['disponível'] == False:
            print(f'O livro "{name_book}" não está disponível para empréstimo!')
        else:
            self.books[name_book]['disponível'] = False
            print('O livro "{}" foi emprestado com sucesso!'.format(name_book))

    def devolver_livros(self, name_book):
        if name_book not in self.books:
            print('O livro {} não existe na biblioteca!'.format(name_book))
        elif self.books[name_book]['disponível'] == True:
            print('O livro "{}" não existe na biblioteca!'.format(name_book))
        else:
            self.books[name_book]['disponível'] = True
            print('O livro "{}" foi emprestado com sucesso!'.format(name_book))
    
    def verificar_disponibilidade(self, name_book):
        if name_book not in self.books:
            print('O livro "{}" não está disponível na Biblioteca!'.format(name_book))
        elif self.books[name_book]['disponível']:
            print('O livro "{}" está disponível para empréstimos!'.format(name_book))
        else:
            self.books[name_book]['disponível']
            print('O livro "{}" não está disponível nesse momento!'.format(name_book))

biblioteca = Biblioteca()

biblioteca.cadastrar_livros("Don't hurt me")
biblioteca.cadastrar_livros('1984')
biblioteca.cadastrar_livros('Harry Potter')
biblioteca.cadastrar_livros('The Art of War')
biblioteca.cadastrar_livros("The Midnight Library")

biblioteca.emprestar_livro('1984')
biblioteca.emprestar_livro('1987')

biblioteca.devolver_livros("Harry Potter")

biblioteca.verificar_disponibilidade("Don't hurt me")





