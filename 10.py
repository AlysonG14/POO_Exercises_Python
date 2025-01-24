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
                'Páginas de Livro: {}'.format(self.título, self.autor, self.número_páginas_livro))
    
    def emprestar(self):
        emprestar = ''
        while emprestar not in ['sim', 'não']:
            print('Olá, seja-bem vindo ao nossa Biblioteca do Alyson')
            empréstimo = input('Você me emprestaria esse livro: {} (sim/não)? '.format(self.título))
            if empréstimo == 'sim':
                self.disponível = True
                print('Sim? Ótimo, muito, obrigado')
            else:
                print('Não? Sério, que coisa hein!! TCHAU!!!')


    def devolver(self):
        devoluçao = ''
        while devoluçao not in ['sim', 'não']:
            devoluçao = input('Deseja fazer uma devolução desse livro: {} (sim/não)? '.format(self.título))
            if devoluçao == 'sim':
                self.disponível = True
                print('Sim? Obrigado, volte sempre!')
            else:
                print('Não? Então tá bom, volte sempre!')

    def verificação(self):
        if self.disponível:
            print('O livro: {} está disponível'.format(self.título))
        else:
            print('O livro: {} não está disponível')


resultado = Livro('A Revolução dos Bichos', 'George Orwell', 152)
print(resultado)

resultado.emprestar()
resultado.devolver()
resultado.verificação()