#%%
#un iterador debe implementar el metodo iter
#puede ser de forma implicita(POO) o explicita(funciones)

#ejerccios
#%%
"""1. Programe una función generadora que retorne los caminos que existen
para llegar de un punto A a un punto B en una matriz de nxm."""
from operator import index
from random import randint

POS_0 = [0, 0]
POS_F = [3, 4]
M, N = 8, 9

def generar_matriz(m, n, pos_0, pos_f):
    matriz = []
    for i in range(m):
        matriz.append([])
        for j in range(n):
            if (i,j) == tuple(pos_0):
                matriz[i].append('1')
            elif (i,j) == tuple(pos_f):
                matriz[i].append('X')
            else:
                matriz[i].append('0')
    return matriz

MATRIZ = generar_matriz(M, N, POS_0, POS_F)
MOVIMIENTOS = ['<-', '->', 'A', 'V']

def aleatorio_number():
    return randint(1,9)

def mostrar():
    for i in MATRIZ:
        print(i)

def alinear(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return x

def wall_function(pos_0, pos_f):
    global MATRIZ
    while pos_0 != pos_f:
        x, y = pos_f[0] - pos_0[0], pos_f[1] - pos_0[1]
        MATRIZ[pos_0[0]][pos_0[1]] = '.'
        if aleatorio_number() % 2 == 0:
            pos_0[0] = pos_0[0] + alinear(x)
            #yield MOVIMIENTOS[1] if x > 0 else MOVIMIENTOS[0]
        else:
            pos_0[1] = pos_0[1] + alinear(y)
            #yield MOVIMIENTOS[1] if y > 0 else MOVIMIENTOS[0]
        MATRIZ[pos_0[0]][pos_0[1]] = '1'
        print(f'x:{x}, y:{y}')

mostrar()

f = wall_function(POS_0, POS_F)
print('----')
mostrar()
"""2. Programe una función que retorne un iterador con los n primeros
números primos, donde n es un número suministrado como argumento."""
#%% 
def is_prime(number):
    for i in number:
        count = 0
        j = 1
        while j <= i:
            if i % j == 0:
                count = count + 1
            j = j + 1
        if count <= 2:
            yield i

f = is_prime(range(1, 35))

for i in range(5):
    print(f.__next__())


"""3. Programe la función generadora par_transpuesta () que opera sobre
una matriz y cuyo resultado es otra matriz donde cada fila es una
columna par de la matriz suministrada como argumento. """
#%%
from random import randint
M, N = 8, 9

def mostrar_i(iterable):
    for i in iterable:
        print(f'{i} *')
    
def aleatorio_number():
    return randint(1,9)

def generar_matriz(m, n):
    matriz = []
    for i in range(m):
        matriz.append([])
        for j in range(n):
            matriz[i].append(aleatorio_number())
    return matriz

def generar_par_transpuesta_filas(matriz):
    aux = 1
    for i in matriz:        
        if aux % 2 == 0:
            yield i
        aux = aux + 1

def generar_par_transpuesta(matriz):
    for i in range(1,N,2):
        yield [fila[i] for fila in matriz]

def sacar_transpuesta(columnas):
    print(f'{columnas}  {len(columnas)}')
    # matriz_t = []
    # for i in range(m):
    #     matriz.append([])
    #     for j in range(n):
    #         matriz[i].append(aleatorio_number())
    # return matriz

matriz = generar_matriz(M, N)
mostrar_i(matriz)
print('--------')
f = generar_par_transpuesta(matriz)
#f_aux = generar_par_transpuesta(matriz)
mostrar_i(f)

# count = 0
# for i in f_aux:
#     sacar_transpuesta(i)
#     count = count + 1
# print(count)


# %%
