from Cliente import Cliente

class Juridico(Cliente):

    def __init__(self, nome = None, cnpj = None):
        super().__init__(nome)
        self.cnpj = cnpj
    
    def cadastrar(self):
        self.nome = input( "Razão Social: ")
        self.limite = float( input("Digite o limite: ") )
        self.cnpj = input( "Digite o CNPJ: ")

    def __str__(self):
        txt = "Razão Social: " + self.nome
        txt += "\nLimite: R$" + str( self.limite )
        txt += "\nCNPJ: " + self.cnpj
        return txt
