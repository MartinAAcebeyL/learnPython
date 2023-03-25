import numpy as np
"""arrays"""

array = np.array([7,5,6,56,1])
#print(array)

array_with_kind = np.array([1,2,3,45],dtype=int)

array_with_ceros = np.zeros(10, dtype=int)
#print(array_with_ceros)

ROWS = 3
COLUMNS = 5
array_rellenado = np.full((ROWS, COLUMNS), 7)
#print(array_rellenado)

use_range = np.arange(0, 25,3)
#print(use_range)

"""copy array"""
other_array = use_range[4:].copy()
#print(other_array)

"""modificar arrays"""
array = np.arange(0,15)
matriz_5x3= array.reshape((5,3))
#print(matriz_5x3)

"""concatenar"""
x = np.arange(0,5)
y = np.arange(5,10)

xy= np.concatenate([x,y])
#print(xy)

matriz = np.array([x,y])
#print(matriz)

matriz1 = np.concatenate([matriz, matriz])
#print(matriz1)

"""convertir de una lista a un array"""
def lis_array():
    lista = [7,5,6,8,96,"hola"]
    x = np.array(lista)
    print(x)
    #saber el tipo de dato del array
    print(x.dtype)
    print(x.shape)

if __name__ == "__main__":
    lis_array()