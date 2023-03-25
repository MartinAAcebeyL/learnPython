import pandas as pd
from pandas import Series, DataFrame
import numpy as np

#series de una unica dimencion
obj = pd.Series([4,5,6,9,22])#declarar una serie
#print(obj)

#print(obj.index)#nos da informacio de la serie
obj2=pd.Series([4,55,62], index=['a','b','c'])#cambiando los indices
#print(obj2)

#print(obj2['b'])#accediendo a los valores
#print(obj2[obj2>60])#accediendo a los valores con condiciones

#print(obj*2)#multiplicamos toda la serie

#print('e' in obj2)# vemos si esta com indice

dic={'a':4,'b':2,'c':8}

obj3 = pd.Series(dic)
#print(obj3)