class Empresa:
    def __init__(self):
        self.historico = []
       


class RH (Empresa):
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
           
    def operacoes (self):
        print("1 - Cadastrar funcionário")
        print("2 - consulta informações do funcionário")
        print("3 - alterar informações do funcionário")
        print("4 - remover informações do funcionário")
        self.operacao = int(input("Digite a operação que você deseja: "))
        
        match self.operacao:
            case 1:
                cadastar = input("Digite o nome do funcionario para cadastrar: ") 
                self.historico.append(cadastar)
                print("Usuario cadastrado")
                return cadastar
            
            case 2:
                consulta = input("Digite o nome do funcionário que você deseja consultar: ")
                for funcionario in self.historico:
                    if funcionario == consulta:
                        print(f"funcionario que você esta procurando é {funcionario}")
                        return consulta
                self.historico.append(consulta)
                return consulta
            
            case 3:
                alteracao = input("Digite o nome do funcionario que você deseja alterar as informações: ")
                self.historico.append(alteracao)
                return alteracao
            
            case 4:
                remocao = input("Digite o nome do funcionário que você deseja remover as informações:")
                for funcionario in self.historico:
                    if remocao == funcionario:
                        self.historico.remove()
                self.historico.append(remocao)
                return remocao
            
    def interacoes (self):
        return self.historico



