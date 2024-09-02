from Cidade import Cidade
from Pessoa import Pessoa

from Categoria import Categoria
from Produto import Produto

from Pedido import Pedido

cid01 = Cidade()
cid02 = Cidade("Porto Alegre")

cli01 = Pessoa("João")
cli02 = Pessoa("Maria", 1.82)
cli03 = Pessoa("José", cid = cid01 )

cat01 = Categoria()
cat02 = Categoria("Alimentos")

prod01 = Produto("Coca-Cola")
prod02 = Produto("Fanta", 8.65)
prod03 = Produto("Arroz", 5.95, cat02)
prod04 = Produto("Pepsi", cat = cat01)
#prod05 = Produto("Trakinas", cat02)

ped01 = Pedido("Rua A")
ped02 = Pedido("Rua B", cli02)


# soma = 0
# soma += ped01.addProduto(prod01)
# soma += ped01.addProduto(prod02)
# print( soma )

print( ped01 )
ped01.addProduto(prod01)
print( ped01.addProduto(prod02) )
ped01.addProduto( prod04 )
ped01.imprimir()










