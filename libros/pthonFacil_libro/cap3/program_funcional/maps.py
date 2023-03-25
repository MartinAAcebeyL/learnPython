#%%
cubicos = lambda x: pow(x,3)
mapa = map(cubicos, [1,2,3])#return a iterable
print(mapa)
for i in mapa:
    print(i)
# %%
suma = lambda a,b,c: a+b+c
mapa1 = map(suma,[7,5,5],[4,5,0], [78,6,5])
for i in mapa1:
    print(i)
# %%
