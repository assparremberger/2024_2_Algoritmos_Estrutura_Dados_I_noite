from No import No

class Fila:

    def __init__(self):
        self.inicio  = None
        self.fim = None

    def add(self, valor):
        nodo = No( valor )
        if self.inicio == None:
            self.inicio = nodo
            self.fim = nodo
        else:
            self.fim.prox = nodo
            self.fim = nodo
        self.imprimir()

    def imprimir(self):
        print("------------------------")
        if self.inicio == None:
            print("Fila está vazia!")
        else:
            aux = self.inicio
            text = ""
            while aux:
                text += aux.dado + " - "
                aux = aux.prox
            print( text )
        print("------------------------")  

    def remover(self):
        if self.inicio == None :
            print("Nenhum elemento removido!")
        else:
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None
        self.imprimir()
