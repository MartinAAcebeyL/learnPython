from math import *
from datetime import date
PI = 3.1415

def triangulo():
    print("de 3 numeros")
    a = float(input())
    b = float(input())
    c = float(input())

    if a + b >= c and a + c >= b and b + c >= a:
        perimetro = (a + b + c)/2
        area = sqrt(perimetro*(perimetro-a)*(perimetro-b)*(perimetro-c))
        print(round(area,3))
    else:
        print("no forma un triangulo")

def calcu(num1, num2, sign = '+'):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1 / num2
    elif sign == '%':
        return num1 % num2
    else:
        print("error")

def trianguloRec():
    print("de los lados")
    a = float(input())
    b = float(input())

    if a <= 0 or b<=0:
        print("no hay solucion")
    else:
        h = sqrt(a**2+b**2)
        angulo = 180/ PI* asin(a/h)
        print("hipotenosa angulo angulo2")
        print(round(h,3),round(angulo,3),round(90-angulo,3))
def anos():
    ahora = date.today()
    ano=int(input("de el año: "))
    mes=int(input("de el mes: "))
    dia=int(input("de el dia: "))

    nacimiento=date(ano,mes,dia)

    comparacion = ahora.year- nacimiento.year
    if comparacion<1:
        print(ahora.month-nacimiento.month,ahora.day-nacimiento.day)
    else:
        print(comparacion)
def fecha():
    fechas=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
    dia = int(input("de el dia "))
    fecha = str(input("de la fecha "))
    ano = int(input("de el año "))
    existe = fechas.count(fecha) 
    if existe>0:
        existe=fechas.index(fecha) + 1
    texto="{} {} del {}".format(dia,existe,ano)
    print(texto)

def funcion():
    return "Hola Mundo"

def llamada_de_retorno(func=""):
    """Llamada de retorno a nivel global"""
    return globals()[func]("Laura")

if __name__=="__main__":#88
    cadena = "bienvenido a mi aplicación".capitalize()
    print(cadena.center(150, "="))

    print(cadena.center(50, " "))
