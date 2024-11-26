def calcular(x, y):
    return x+y , x-y , x*y , x/y

print( calcular(6,2) )

soma, sub, mult, div = calcular( 9 , 3 )
print("Soma: " , soma)
print("Subtração: " , sub)
print("Multiplicação: " , mult)
print("Divisão: " , div)
result = calcular( 10 , 5)
print("Multiplicação: " , result[2] )
