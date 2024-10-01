import sys
from PyQt5.QtWidgets import *
from Categoria import Categoria
from Veiculo import Veiculo
from FormCategoria import FormCategoria

class FormVeiculo(QMainWindow):
    def __init__(self, veiculos = [], categorias = [], telaCategoria = None):
        super().__init__()
        self.veiculos= veiculos
        self.categorias = categorias
        self.formCategoria = telaCategoria
        if self.formCategoria is not None:
            self.formCategoria.formVeiculo = self

        self.setWindowTitle( "Cadastro de Veículo")
        self.setGeometry(350, 100, 300, 250)
        self.layout = QVBoxLayout()
        self.definirLayout()

        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )

    def definirLayout(self):
        self.lblModelo = QLabel("Modelo: ")
        self.txtModelo = QLineEdit(self)
        self.txtModelo.setPlaceholderText("Digite o modelo do veículo")
        self.txtModelo.setMaxLength(8)
        self.layout.addWidget( self.lblModelo )
        self.layout.addWidget( self.txtModelo )

        self.lblPlaca = QLabel("Placa: ")
        self.txtPlaca = QLineEdit(self)
        self.txtPlaca.setPlaceholderText("XXX-0X00")
        self.layout.addWidget( self.lblPlaca )
        self.layout.addWidget( self.txtPlaca )

        self.lblKM = QLabel("Kilometragem: ")
        self.txtKM = QLineEdit(self)
        self.txtKM.setPlaceholderText("0000")
        self.layout.addWidget( self.lblKM )
        self.layout.addWidget( self.txtKM )

        # self.btnCarregarCategorias = QPushButton("Atualizar Categorias", self)
        # self.btnCarregarCategorias.clicked.connect( self.carregarCategorias )
        # self.layout.addWidget( self.btnCarregarCategorias )


        self.lblCategoria = QLabel("Categoria: ")
        self.layout.addWidget( self.lblCategoria )

        self.cmbCategoria = QComboBox(self)
        self.cmbCategoria.currentIndexChanged.connect( self.adicionarCategoria )
        self.carregarCategorias()
        self.layout.addWidget( self.cmbCategoria )

        self.chbAutomatico = QCheckBox("Automático")
        self.layout.addWidget( self.chbAutomatico )

        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect( self.salvar )
        self.layout.addWidget( self.btnSalvar )

    def carregarCategorias(self):
        self.cmbCategoria.clear()
        self.cmbCategoria.addItem( "Selecione...", None )
        self.cmbCategoria.addItem( "Adicionar Categoria...", None )
        for c in self.categorias:
            self.cmbCategoria.addItem( c.nome , c)


    def salvar(self):
        modelo = self.txtModelo.text()
        if len(modelo)  > 0 :
            veiculo = Veiculo( modelo )
            if len( self.txtPlaca.text() ) > 0:
                veiculo.placa = self.txtPlaca.text()
            if self.cmbCategoria.currentIndex() > 1:
                veiculo.categoria = self.cmbCategoria.currentData()

            if len( self.txtKM.text() ) > 0:
                veiculo.kilometragem = int( self.txtKM.text() )

            veiculo.automatico = self.chbAutomatico.isChecked()
            
            self.veiculos.append( veiculo )
            QMessageBox.information(self, "Veículo Salvo" , str(veiculo))

    def adicionarCategoria(self):
        if self.cmbCategoria.currentIndex() == 1: 
            self.formCategoria.show()
 