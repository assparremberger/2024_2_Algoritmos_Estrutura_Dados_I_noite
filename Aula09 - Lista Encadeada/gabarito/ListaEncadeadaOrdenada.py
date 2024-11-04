from No import No

class ListaEncadeadaOrdenada:

    def __init__(self):
        self.inicio = None

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

    def add(self, valor):
        nodo = No( valor )
        if self.inicio == None:
            self.inicio = nodo
        elif nodo.dado < self.inicio.dado:
            nodo.prox = self.inicio
            self.inicio = nodo
        else:
            ant = self.inicio
            aux = self.inicio.prox
            while aux:
                if nodo.dado < aux.dado:
                    nodo.prox  = aux
                    ant.prox = nodo
                    break
                else:
                    ant = aux
                    aux = aux.prox
            if aux == None:
                ant.prox = nodo
        self.imprimir()

    def remover(self, valor):
        if self.inicio == None:
            print("Nenhum elemento removido")
        else:
            encontrou = False
            if valor == self.inicio.dado:
                encontrou = True
                self.inicio = self.inicio.prox
            else:
                ant = self.inicio 
                aux = self.inicio.prox
                while aux:
                    if valor == aux.dado:
                        encontrou = True
                        ant.prox = aux.prox
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if encontrou:
                print( valor , " encontrado e removido!")
            else:
                print( "-------------------------------")
                print( valor , " não foi encontrado!")
        self.imprimir()
            

        





