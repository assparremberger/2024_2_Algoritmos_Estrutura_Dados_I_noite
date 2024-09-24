import sys
from PyQt5.QtWidgets import *
from Cidade import Cidade
from Pessoa import Pessoa

class FormCliente(QMainWindow):
    def __init__(self, titulo="Formulário de Cliente", pessoas = [], cidades = []):
        super().__init__()
        self.cidades = cidades
        self.clientes = pessoas

        self.setWindowTitle(titulo)
        self.setGeometry(350, 100, 300, 200)
        self.layout = QVBoxLayout()
        self.definirLayout()

        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )

    def definirLayout(self):
        self.lblNome = QLabel("Nome do cliente: ")
        self.txtNome = QLineEdit(self)
        self.txtNome.setPlaceholderText("Informe o nome do cliente")
        self.txtNome.setMaxLength(20)
        self.layout.addWidget( self.lblNome )
        self.layout.addWidget( self.txtNome )

        self.lblAltura = QLabel("Altura: ")
        self.txtAltura = QLineEdit(self)
        self.layout.addWidget( self.lblAltura )
        self.layout.addWidget( self.txtAltura )

        self.lblCidade = QLabel("Cidade: ")
        self.layout.addWidget( self.lblCidade )

        self.cmbCidade = QComboBox(self)
        self.cmbCidade.addItem( "Selecione...", None )
        for c in self.cidades:
            self.cmbCidade.addItem( c.nome , c)

        self.layout.addWidget( self.cmbCidade )
        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect( self.salvar )
        self.layout.addWidget( self.btnSalvar )

    def salvar(self):
        nome = self.txtNome.text()
        if len(nome)  > 0 :
            cli = Pessoa(nome)
            if len( self.txtAltura.text() ) > 0:
                sAltura = self.txtAltura.text().replace("," , ".")
                cli.altura = float( sAltura )
            if self.cmbCidade.currentIndex() > 0:
                cli.cidade = self.cmbCidade.currentData()
            self.clientes.append( cli )
            QMessageBox.information(self, "Cliente Salvo" , str(cli))