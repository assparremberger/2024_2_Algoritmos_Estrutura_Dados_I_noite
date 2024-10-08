from abc import ABC, abstractmethod

class Cliente( ABC ):

    def __init__(self, nome):
        self.id = None
        self.nome = nome
        self.__limite = 0.0

    def __str__(self):
        txt = "Nome: " + self.nome
        txt += "\nLimite: R$" + str(self.__limite)
        return txt

    def imprimir(self):
        print( self )

    @abstractmethod
    def cadastrar(self):
        pass

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        if valor >= 0.0 and valor <= 1000.0:
            self.__limite = valor
        else:
            print( "Valor não permitido!")


        