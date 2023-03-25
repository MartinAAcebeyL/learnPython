import pandas as pd
from pandas import Series, DataFrame
import numpy as np

"""---dataframes, de mas dimenciones"""

data = {'id':[101,102,103,104],'names':['raul','paul','saul','maul'],'precio':[4,5,66,30], 'sex': ['M', 'M', 'M','M'], 'age':[25,45,18,62]}
#print(data)

frame=pd.DataFrame(data)#convirtiendo a dataframe
#print(frame)

#cambiando o agregando columnas
print(pd.DataFrame(data, columns=['precio','id','otros']))

#para que nos muestre una columna
#print(frame.nombres)
#print(frame['precio'])

#print(frame.loc[0])#para obtener filas

locations=['sucre','cbba','potosi', 'oruro']
frame['locations']=locations
#print(frame)#add a new column

transpuest_frame=frame.T#transpuesta
#print(transpuest_frame)

valores = frame.values#da los valores del frame
#print(valores)

index = frame.index#los indices
#print(index)

#un datafreme son inmutables

""""--Filtros--"""

may_40 = frame.loc[:,'age'] >= 40#filtrando a los mayores a 10
may_40 = frame.loc[may_40]
#print(may_40)

male = frame.loc[:, 'sex'] == 'M'
male = frame.loc[male]
male.head(2)
#print(male)

"""agrupamiento"""#--> no entiendo, no explica bien
df = pd.DataFrame({'key1':['a', 'a', 'b','b','a'],'key2':['one','two','one','two','one'],'value1':[4,3,33,2,11],'value2':[75,65,45,43,12]})
group = df['value1'].groupby(df['key1'])
#print(group)
#print(group.mean())

"""agrupaciones con array"""

years = np.array([2000,2000,2001,2020,2012])
countries = np.array(['pt', 'pt', 'scz', 'scz', 'lp'])
group1 = df['value1'].groupby([years, countries]).mean()
#print(group1)
"""iteraciones con ordenamiento"""#--> no entiendo, no explica bien

for name, add in df.groupby('key1'):
    pass
    #print(name)
    #print(add)
