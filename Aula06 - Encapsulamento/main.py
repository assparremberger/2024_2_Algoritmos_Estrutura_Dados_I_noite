import sys
from PyQt5.QtWidgets import QApplication
from FormVeiculo import FormVeiculo
from FormCategoria import FormCategoria

app = QApplication(sys.argv)


#from Categoria import Categoria

listaCategorias = []
listaVeiculos = []

formCategoria = FormCategoria( categorias = listaCategorias )

form = FormVeiculo( veiculos= listaVeiculos,  categorias= listaCategorias, telaCategoria=formCategoria )
form.show()

sys.exit( app.exec_() )





