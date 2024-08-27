class Categoria:

    def __init__(self, nome = "Bebidas"):
        self.id = None
        self.nome = nome

    def __str__(self):
        return "Id: " + str(self.id) + " - Nome: " + self.nome