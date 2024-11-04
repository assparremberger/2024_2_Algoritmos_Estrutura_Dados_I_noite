from No import No

class ListaEncadeada:

    def __init__(self):
        self.inicio = None

    def addInicio(self, valor):
        nodo = No( valor) 
        if self.inicio is not None:
            nodo.prox = self.inicio
        self.inicio = nodo
        self.imprimir()

    def addFim(self, valor):
        nodo = No( valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.imprimir()
    
    def imprimir(self):
        print("------------------------")
        if self.inicio == None:
            print("Lista Encadeada está vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox
        print("------------------------")

    def removerInicio(self):
        if self.inicio == None:
            print("Nenhum elemento removido")
        else:
            self.inicio = self.inicio.prox
        self.imprimir()

    def removerFim(self):
        if self.inicio == None:
            print("Nenhum elemento removido")
        else:
            if self.inicio.prox == None:
                self.inicio = None
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux.prox:
                    ant = aux
                    aux = aux.prox
                ant.prox = None
        self.imprimir()


