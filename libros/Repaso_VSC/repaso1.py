'''print("Operaciones matematicas basicas")
numero1=3
numero2=4

suma=numero1+numero2
resta=numero1-numero2
division=numero1/numero2
divisionEnteros=numero1/numero2
multiplicaion=numero1*numero2
exponencial=numero1**numero2
residuo=numero1%numero2

print("suma: " ,suma)
print("resta: ",resta)
print("multi: ",multiplicaion)
print("divis: ",divisionEnteros)
print("expo: " ,exponencial)'''

print("Manejo de String's")

'''
#concatenando
mensaje1="hola " 
mensaje2='soy' 
mensaje3=" Martin"
m=mensaje1+mensaje2+mensaje3#manera 1
print(m+"\n'el PRo'")

var="hola"
var1="HOLA"
m="Pesonaje1: %s \nPersonaje2: %s"%(var,var1)#manera 2
print(m)

m="\nPersonaje1: {}\nPersonaje2: {}".format(var1,var)#manera 3
print(m)

#6 String como listas
#em python los strings si cuenta desde la posicion 0

var="hola soy martin, como estan"
print(var[5]+var[0],var[-1])#ojo con los ',' y '+'
print(var[0:6])#saca un trozo 
print(var[0:15:3])#escoje cada 3
print(var[::-1])#reverse
'''
'''Formato'''
'''
var="soy Martin"
var1="empresario"
var2="solitario"

m="{} {} {}".format(var,var1,var2)
m1="{} {} {c}".format(var,"padre",c=var2)
print(m,"\n"+m1+"\n")#las comas dan un espacio mas, las sumas no

mayuscula=m.upper()
minuscula=m.lower()
titulo=m.title()
print(mayuscula,minuscula,titulo)'''

'''BUSQUEDA'''
c="tu"
m="{} {} {}".format("hola","soy",c)
print(m)

posicion=m.find('tu')
conteo=m.count('q')
print(posicion,conteo)

'''OTROS'''
remplazo=m.replace('h',"po")
nose=m.split('o')
nose1=m.split(' ')
print(remplazo)
print(nose,nose1)