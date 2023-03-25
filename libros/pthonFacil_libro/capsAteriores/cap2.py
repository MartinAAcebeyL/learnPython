from functools import reduce #para usar reduce
from itertools import filterfalse

class p(object):
    __slots__=['a','b']#restringe los atributos

var=p()
var.a=78
#print(var.a)

#var.c=123
#print(var.c)

"""funcion map"""
f=lambda x,y:x*y
d=map(f,[1],[3,2])

for i in d:
    pass
    #print(i)

"""funcion reduce4"""
ff=lambda x,y:x*y
#print(reduce(ff,[2,4,3]))

"""funcion filter"""
filtrar=lambda x:x%2==0
f=filter(filtrar,[1,2,3,4,5])
for i in f:
    pass
    #print(i)

fff=filterfalse(filtrar,[1,2,3,4,5])#lo contrario que la funcion lambda filtrar
for i in fff:
    pass
    #print(i)

