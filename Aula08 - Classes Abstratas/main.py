#from Cliente import Cliente
#c = Cliente("João")
from Fisico import Fisico
from Juridico import Juridico

c = Fisico("João", "000.111.222-33")
c.imprimir()
print("-------------------")
pj = Juridico()
pj.cadastrar()
pj.imprimir()