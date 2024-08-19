#Método que tem retorno e não recebe parâmetro
def getPI():
    return 3.14
    
#Método que não tem retorno e não recebe parâmetro
def imprimirPI():
    print( getPI() )

#Método que tem retorno e recebe parâmetro
def calcularAreaCirculo(raio):
    area = getPI() * ( raio * raio )
    return area

#Método que não tem retorno e recebe parâmetro
def imprimirAreaCirculo( radius ):
    print( calcularAreaCirculo( radius ) )      





