import sys
from PyQt5.QtWidgets import *
from TelaProduto import TelaProduto

class TelaPerecivel(TelaProduto):

    def __init__(self, titulo="Tela de Produto Perecível"):
        super().__init__(titulo)

    def definirLayout(self):
        super().definirLayout()
        self.lblTemperatura = QLabel("Temperatura Máximo:")
        self.txtTemperatura = QLineEdit(self)
        self.layout.addWidget( self.lblTemperatura )
        self.layout.addWidget( self.txtTemperatura )

    def salvar(self):
        nome = self.txtNome.text()
        preco = self.txtPreco.text()
        txt = "Nome: " + nome
        txt += "\nPreço: " + preco
        txt += "\nTemperatura Máxima: " + self.txtTemperatura.text()
        QMessageBox.information(self, "Produto Salvo", txt )