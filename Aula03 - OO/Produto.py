from Categoria import Categoria

class Produto:

    def __init__(self, nome, preco = 0.0, cat = Categoria("Outra") ):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.categoria = cat