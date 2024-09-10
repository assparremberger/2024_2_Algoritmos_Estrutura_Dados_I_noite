from Produto import Produto
from Categoria import Categoria

class Perecivel( Produto ):

    def __init__(self, nome, preco = 1.99, cat = Categoria("Perecíveis"), temperatura = 8):
        super().__init__(nome, preco, cat)
        self.temperatura = temperatura

    def __str__(self):

        txt = "Perecível " + super().__str__()
        # txt = "Perecível: "
        # txt += "\nNome: " + self.nome
        # txt += "\nPreço: " + str(self.preco)
        # txt += "\nCategoria: " + self.categoria.nome
        txt += "\nTemperatura: " + str(self.temperatura)
        return txt


#prod = Perecivel("Baré Cola", 9.99, Categoria("Antigos"), 7.5)
#print( prod )



