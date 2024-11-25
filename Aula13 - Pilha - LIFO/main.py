from Pilha import Pilha
from Livro import Livro


pilha = Pilha()

pilha.imprimir()

l1 = Livro("Dom Casmurro" , "Machado de Assis", 100)
l2 = Livro("Memórias Póstumas de Brás Cubas" , "Machado de Assis", 100)
l3 = Livro("O Tempo e o Vento" , "Érico Veríssimo", 100)

pilha.add( l2 )
pilha.add( l1 )
pilha.add( l3 )

pilha.remover()