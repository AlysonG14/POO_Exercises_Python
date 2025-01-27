class RedeSocial:
    def __init__(self):
        self.usuarios = {}

    def adicionar(self, nome):
        if nome in self.usuarios:
            print(f'Usuário {nome} já existe na sua rede social!')
        else:
            self.usuarios[nome] = {'amigos': [], 'posts': []}
            print(f'Usuário {nome} adicionado com sucesso!')

    def adicionar_amigos(self, usuario1, usuario2):
        if usuario1 not in self.usuarios or usuario2 not in self.usuarios:
            print('Um dos usuários não existe')
        elif usuario2 in self.usuarios[usuario1]['amigos']:
            print(f'{usuario1} e {usuario2} já são amigos.')
        else:
            self.usuarios[usuario1]['amigos'].append(usuario2)
            self.usuarios[usuario2]['amigos'].append(usuario1)
            print(f'{usuario1} e {usuario2} agora são amigos.')

    def publicar_mensagem(self, usuario, mensagem):
        if usuario not in self.usuarios:
            print(f'O usuário {usuario} não existe')
        else:
            self.usuarios[usuario]['posts'].append({'mensagem': mensagem, 'comentarios': []})
            print(f'{usuario} publicou: {mensagem}')

    def comentar_post(self, usuario, mensagem, comentario):
        if usuario not in self.usuarios:
            print(f'O usuário {usuario} não existe.')
            return
        for user, data in self.usuarios.items():
            for post in data['posts']:
                if post['mensagem'] == mensagem:
                    post['comentarios'].append({'usuario': usuario, 'comentario': comentario})
                    print(f'{usuario} comentou: "{comentario}" no post de {user}')
                    return
        print('Post com a mensagem não encontrado.')

    def buscar_usuario(self, nome):
        if nome in self.usuarios:
            print(f'Usuário {nome} encontrado com sucesso!')
        else:
            print('Usuário não encontrado!')


rede = RedeSocial()
rede.adicionar('Leonardo')
rede.adicionar('Douglas')
rede.adicionar_amigos('Douglas', 'Leonardo')
rede.publicar_mensagem('Douglas', 'Oi, como vocês estão?')
rede.comentar_post('Leonardo', 'Oi, como vocês estão?', 'E aí, Douglas!')
rede.buscar_usuario('Alyson')  