'''
Exercise 24 - Desenvolva um sistema de gestão de um zoológico, com classes para Animal, Habitat, Alimentação, Veterinário, e Funcionário. Cada tipo de animal terá características específicas, como dieta e necessidades ambientais, e o sistema deve permitir o controle de alimentação, saúde e movimentação dos animais.
'''

class Zoológico:
    def __init__(self, nome):
        self.nome = nome


class Animal(Zoológico):
    def __init__(self, nome, raça, dieta, habitat):
        super().__init__(nome)
        self.nome = nome
        self.raça = raça
        self.dieta = dieta
        self.habitat = habitat
        self.saude = 'Saúdavel'

    def alimentar(self, alimentação):
        print('O animal {} foi alimentado com {}'.format(self.nome, alimentação))

    def mover(self, habitat):
        print(f'O animal {self.nome} foi movido através de {habitat.tipo}')
        self.habitat = habitat

    def verificar_saude(self):
        if self.saude == 'Saudável':
            print('O animal {} está saudável.'.format(self.nome))
        else:
            print('O animal {} não está saudável.'.format(self.nome))

    def veterinário(self, veterinario):
        print(f'O animal {self.nome} está sendo tratado pelo veterinário {veterinario.nome} ({veterinario.especialidade})')
        self.saude = 'Saudável'



class Habitat(Zoológico):
    def __init__(self, temperatura, tipo, umidade):
        super().__init__(tipo)
        self.temperatura = temperatura
        self.tipo = tipo
        self.umidade = umidade

class Alimentacao(Zoológico):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo

    def __str__(self):
        return f'Alimento {self.nome}, Tipo: {self.tipo}'

class Veterinário(Zoológico):
    def __init__(self, nome, especialidade):
        super().__init__(nome)
        self.especialidade = especialidade

class Funcionário(Zoológico):
    def __init__(self, nome, carga):
        super().__init__(nome)
        self.carga = carga

    def desempenhar_função(self, função):
        print('O funcionário {}, com carga de {}, está {}'.format(self.nome, self.carga, função))


habitat_savanna = Habitat('Savanna', 30, 40)
habitat_floresta = Habitat('Floresta', 25, 60)

tigre = Animal('Tigre', 'Panthera tigris', 'Carnes', habitat_savanna)
macaco = Animal('Macaco', 'Cebidae', 'Frutas', habitat_floresta)

carne = Alimentacao('Carne', 'Proteica')
fruta = Alimentacao('Banana', 'Frutas')

veterinario = Veterinário('Dr. Alyson', 'Exótico')

funcionario = Funcionário('David', 'Médico')

funcionario.desempenhar_função('alimentando os animais')
tigre.alimentar(carne)
macaco.alimentar(fruta)
tigre.mover(habitat_floresta)
tigre.veterinário(veterinario)  
