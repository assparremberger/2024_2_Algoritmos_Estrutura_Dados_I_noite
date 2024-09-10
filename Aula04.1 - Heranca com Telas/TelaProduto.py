import sys
#from PyQt5 import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import *

class TelaProduto(QMainWindow):
    def __init__(self, titulo="Tela de Produto"):
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(300, 200, 300, 300)
        self.layout = QVBoxLayout()

        self.definirLayout()

        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect( self.salvar )
        self.layout.addWidget( self.btnSalvar )

        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )


    def definirLayout(self):
        self.lblNome = QLabel("Nome: ")
        self.txtNome = QLineEdit(self)
        self.lblPreco = QLabel("Preço: ")
        self.txtPreco = QLineEdit(self)

        self.layout.addWidget( self.lblNome )
        self.layout.addWidget( self.txtNome )
        self.layout.addWidget( self.lblPreco )
        self.layout.addWidget( self.txtPreco)


    def salvar(self):
        nome = self.txtNome.text()
        preco = self.txtPreco.text()
        txt = "Nome: " + nome
        txt += "\nPreço: " + preco
        QMessageBox.information(self, "Produto Salvo", txt )



