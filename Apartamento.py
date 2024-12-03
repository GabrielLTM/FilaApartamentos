from Torre import Torre

apartamentos_cad = []
class Apartamento:
    def __init__(self, nome, endereco, numero, vaga):
        self.numero = numero
        self.torre = Torre(nome, endereco)
        self.vaga = vaga
        self.proximo = None

       
    def cadastrar(self):
        apartamentos_cad.append(self)
        return f'O apartamento {self.numero} foi cadastrado com sucesso'