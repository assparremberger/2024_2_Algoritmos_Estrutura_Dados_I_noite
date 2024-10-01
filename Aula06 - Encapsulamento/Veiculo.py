from Categoria import Categoria
class Veiculo:

    def __init__(self,modelo=None,placa=None, aut=False, cat = Categoria() ):
        self.id = None
        self.modelo = modelo
        self.placa = placa
        self.automatico = aut
        self.categoria = cat
        self.__kilometragem = 0

    def __str__(self):
        txt = "\nModelo: " + self.modelo
        txt += "\nPlaca: " + self.placa
        txt += "\nCâmbio Automático: "
        if self.automatico:
            txt += "Sim"
        else: 
            txt += "Não"
        txt += "\nCategoria: " + self.categoria.nome
        txt += "\nKilometragem: " + str( self.__kilometragem )
        return txt