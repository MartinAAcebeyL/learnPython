'''listas'''

lista=[1,2,3,'a','g','e',9.0,False,"prro"]
print(lista)
lista.append(True)
print(lista)
lista.insert(0,"xxx")
print(lista)
lista.remove(1)
print(lista)
lista.pop()
print(lista)

listaNumerica=[45,7,6,23,1,0,8,9,4]
print(listaNumerica)
listaNumerica.sort()
print(listaNumerica)
listaNumerica.sort(reverse=True)
print(listaNumerica)

listaNumerica1=[0,9,56,2]
listaNumerica.extend(listaNumerica1)
print(listaNumerica)

'''Tuplas'''
tupla=([4,5,6,3],2.3,'3',2,1,'p',"hola")
print("\n",tupla)
print(tupla[0])
print(tupla[0:5:2])

'''Diccionario'''
diccionario={2:1,'a':4,'r':'p',"hola":'3'}
print("\n",diccionario)
diccionario={2:1,'a':4,'r':'p',"hola":'3',2:'4'}
print(diccionario)
diccionario[7.5]="p"
print(diccionario)
diccionario[2]=(45,46)
print(diccionario)

valor=diccionario[2]
print("valor de la llave '2':",valor)
valor=diccionario.get(20,"no hay")
print(valor)
print(diccionario)
del diccionario[2]
print(diccionario)

llaves=diccionario.keys()
print("\n",llaves)
llaves=list(diccionario.keys())
print(llaves)
valores=diccionario.values()
print(valores)
valores=list(diccionario.values())
print(valores)

llaves=diccionario.keys()
print("\n",llaves)
llaves=tuple(diccionario.keys())
print(llaves)
valores=diccionario.values()
print(valores)
valores=tuple(diccionario.values())
print(valores)

diccionario1={"hola":(7,5,8,9),9:"hola",7:[1,2,7]}
print(diccionario1)
diccionario.update(diccionario1)
print(diccionario)