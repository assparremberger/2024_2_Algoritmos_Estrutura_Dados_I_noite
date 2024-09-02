from Pessoa import Pessoa
from Produto import Produto
from Categoria import Categoria

class Pedido:

    def __init__(self, end, cli = Pessoa("Cliente não informado") ):
        self.id = None
        self.end = end
        self.cliente = cli
        self.__produtos = []

    def addProduto(self, prod):
        if prod is not None:
            self.__produtos.append( prod )
        total = 0.0
        for p in self.__produtos:
            total += p.preco
        return total

    def __str__(self):
        txt = "Produtos: \n"
        for p in self.__produtos:
            txt += "\n------------------"
            txt += "\nNome: " + p.nome
            txt += "\nPreço: " + str(p.preco)
          #  txt += "\nCategoria: " + p.categoria.nome
            txt += "\nCategoria: " + str(p.categoria)
        return txt

    def imprimir(self):
        print( self )


