"""Programe una función que determine si dos listas son iguales. Dos listas se
consideran iguales si tienen igual longitud y sus elementos en cada índice
también lo son."""

"""lista1=(1,2,3)
lista2=(1,2,3)
#
if len(lista1)==len(lista2):
    b=True
    for i in range(0,len(lista1)):
        if(lista1[i]!=lista2[i]):
            b=False
            break
    if b:
        print('iguales')
    else:
        print('else')
else:
    print('else')"""

"""if lista1 == lista2:
    print('listas iguales')
else:
    print('else')"""

"""Programe una función que reciba una matriz de enteros y devuelva una
tupla con la lista o vector de la suma de cada fila y otro vector con la suma
de cada columna."""

"""def suma(m):
    su:float
    lista=[]
    for i in range(0,len(m[0])):
        su=0
        for j in range(0,len(m)):
            su+=m[j][i]
        lista.append(su)
    return lista

m=[[4,5,6,8],
    [0,1,9,3],
    [7,8,9,5]]
#x=suma(m)
print(x)"""

"""Programe una función que determine si un número entero suministrado
como argumento es primo."""

def is_prime(n):
    cont=0
    for i in range(1,n+1):
        if(n%i==0):
            cont+=1
    if(cont>2):
        return False
    return True

#print(is_prime(3))

"""Programe una función que dado un número x devuelva una lista infinita con
todos los múltiplos de x."""

def multiplos(n,x):
    lista=[]
    for i in range(1,x+1):
        m=i*n
        print(str(i)+'*'+str(n)+'='+str(m))
        lista.append(m)
    return lista
print(multiplos(5,10))

"""Diseñe y programe un algoritmo recursivo que encuentre la salida de un
laberinto, teniendo en cuenta que el laberinto se toma como entrada y que
es una matriz de valores True, False, (x,y), (a,b}, donde True indica un
obstáculo; Fa/se, una celda por la que se puede caminar; (x,y), el punto
donde comienza a buscarse la salida y (a,b), la salida del laberinto."""

"""Programe una solución recursiva al conocido juego de las Torres de Hanoi."""
