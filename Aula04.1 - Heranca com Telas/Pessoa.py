from Cidade import Cidade

class Pessoa:

    def __init__(self, nome, altura = 1.73, cid = Cidade(nome = "Itati") ):
        self.id = None
        self.nome = nome
        self.altura = altura
        self.cidade = cid

    def __str__(self):
        txt = "Nome: " + self.nome + "\n"
        txt += "Altura: " + str( self.altura ) + "\n"
        txt += "Cidade: " +  self.cidade.nome
        return txt