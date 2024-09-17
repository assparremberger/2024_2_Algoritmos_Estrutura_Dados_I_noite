import sys
from PyQt5.QtWidgets import *
from FormCidade import FormCidade
from Cidade import Cidade

class TelaPrincipal(QMainWindow):
    def __init__(self, titulo="Lojinha"):
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(100, 50, 200, 200)
        self.layout = QVBoxLayout()

        self.cidades = []
        self.clientes = []

        self.definirLayout()

        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )

        

    def definirLayout(self):
        self.btnAddCidade = QPushButton("Add Cidade", self)
        #self.btnAddCliente =QPushButton("Add Cliente", self)
        self.btnVerCidades = QPushButton("Ver Cidades", self)

        self.btnVerCidades.clicked.connect( self.listarCidades )
        self.btnAddCidade.clicked.connect( self.addCidade )
        #self.btnAddCliente.clicked.connect( self.addCliente )

        self.layout.addWidget( self.btnVerCidades)
        self.layout.addWidget( self.btnAddCidade )
        #self.layout.addWidget( self.btnAddCliente)

    def addCidade(self):
        app = QApplication(sys.argv)
        telaAddCidade = FormCidade( cidades = self.cidades )
        telaAddCidade.show()
        sys.exit( app.exec_() )

    def listarCidades(self):
        txt = ""
        if self.cidades.__len__() == 0:
            txt += "Nenhuma Cidade Cadastrada"
        else:
            for cid in self.cidades:
                txt += "\n" + cid.nome

        QMessageBox.information(self, "Lista de Cidades", txt )


    




