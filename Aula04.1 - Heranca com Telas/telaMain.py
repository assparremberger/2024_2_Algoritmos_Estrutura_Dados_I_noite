import sys
from PyQt5.QtWidgets import QApplication
#from TelaProduto import TelaProduto
from TelaPerecivel import TelaPerecivel
from TelaPrincipal import TelaPrincipal

app = QApplication(sys.argv)
#telaProd = TelaProduto("Cadastro de Produto")
#telaProd.show()

#telaPerecivel = TelaPerecivel()
#telaPerecivel.show()

#tp = TelaPrincipal()
#tp.show()



from Cidade import Cidade
from FormCliente import FormCliente

listaCidades = []

listaCidades.append( Cidade("Porto Alegre") )
listaCidades.append( Cidade("Canoas") )

formCli = FormCliente(pessoas=[], cidades= listaCidades )
formCli.show()

sys.exit( app.exec_() )





