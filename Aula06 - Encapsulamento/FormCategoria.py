import sys
from PyQt5.QtWidgets import *
from Categoria import Categoria

class FormCategoria(QMainWindow):
    def __init__(self, titulo="Formulário de Categoria", categorias = [], telaVeiculo = None):
        super().__init__()
        self.formVeiculo = telaVeiculo
        self.categorias = categorias

        self.setWindowTitle(titulo)
        self.setGeometry(100, 100, 200, 100)
        self.layout = QVBoxLayout()
        self.definirLayout()

        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )

    def definirLayout(self):
        self.lblNome = QLabel("Nome da categoria: ")
        self.txtNome = QLineEdit(self)
        self.layout.addWidget( self.lblNome )
        self.layout.addWidget( self.txtNome )
        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect( self.salvar )
        self.layout.addWidget( self.btnSalvar )

    def salvar(self):
        if len( self.txtNome.text() ) > 0:
            cat = Categoria( self.txtNome.text() )
            self.categorias.append( cat )
            self.txtNome.setText("")

        if self.formVeiculo is not None:
            self.formVeiculo.carregarCategorias()
