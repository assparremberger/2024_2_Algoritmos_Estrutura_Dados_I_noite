def somar(valores):
    soma = 0
    for x in valores:
        soma += x
    return soma

values = ( 5, 2) , (6 , 3) , [ 7, 4, 10] , (8, 2, 1, 5)

resultados = map( somar , values  )
print( list( resultados ) )