"""Programe una clase cuenta_bancaria con los siguientes métodos y
propiedades:
• Método de clase: extraer_dinero(cantidad), que disminuye el saldo de
la cuenta en la cantidad indicada. Deben considerarse situaciones
ilógicas como por ejemplo que se intenta extraer una cantidad negativa
o que la cantidad a extraer es mayor que el saldo actual.
• Método de clase: depositar(cantidad), que aumenta el saldo de la
cuenta en la cantidad indicada. El saldo debe ser una cantidad positiva.
• Método de clase: transferir(cantidad, cuenta), que recibe la cantidad a
transferir y una cuenta adonde realizar la transferencia. Deben considerarse
situaciones ilógicas como por ejemplo que se intenta extraer una cantidad
negativa o que la cantidad a extraer es mayor que el saldo actual.
• Método de clase: extraer_todo(), que deja la cuenta vacía y devuelve el saldo.
• Propiedad: saldo, que devuelve el saldo de la cuenta bancaria.
• Propiedad: nombre_propietario, que devuelve el nombre del dueño de
la cuenta.
• Propiedad: numero_tarjeta, que devuelve el número de la tarjeta
asociada con la cuenta bancaria.
• Propiedad: esta_vacia, que devuelve True si el saldo de la cuenta
bancaria es O y Fa/se en caso contrario."""
from random import randint
from datetime import datetime
import math

class cuenta_bancaria:
    cuenta = 0
    cuenta_lista = []
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        cuenta_bancaria.cuenta += 1
        self.cuenta=cuenta_bancaria.cuenta
        cuenta_bancaria.cuenta_lista.append(self.cuenta)
        self.numero_tarjeta=randint(1000,2000)
        self.esta_vacia = True if saldo <= 0 else False 

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def extraer_dinero(self, cantidad):
        if cantidad <= self.get_saldo():
            self.saldo-=cantidad
            self.esta_vacia = True if self.saldo <= 0 else False 
            return cantidad
        else:
            print('saldo insuficiente' + str(self.get_saldo()) + '\ncantidad solicitada' + str(cantidad))

    def depositar(self, monto:int):
        if monto < 0:
            print('no se puede depositar ese monto' + monto)
        else:
            self.saldo+=monto

    @staticmethod
    def transferir(user_a:object, cantidad:int, user_b:object):
        if cantidad <= user_a.saldo:
            if user_b.cuenta in cuenta_bancaria.cuenta_lista:
                user_a.extraer_dinero(cantidad)
                user_b.depositar(cantidad)
                print('operacion echa')
            else:
                print('la cuenta no existe' + str(user_b.cuenta))
        else:
            print('saldo insuficiente, usted tiene: ' + str(user_a.saldo))
    
    def extraer_todo(self):
        x = self.saldo
        self.set_saldo(0)
        print('cuenta vacia')
        self.esta_vacia = True
        return x

    @classmethod
    def mostrar(cls, *args):
        for i in range(0, len(args)):
            print('user: ' + str(args[i].nombre) + 
            ' cuenta: ' + str(args[i].cuenta) + 
            ' saldo: ' + str(args[i].saldo) + 'numero de tarjeta: ' + str(args[i].numero_tarjeta))

"""Programe una clase fecha con los siguientes métodos:
• Método estático: fecha_ actual(), que devuelve la fecha actual.
• Método estático: hora_actual(), que devuelve la hora actual.
• Método estático: a_fecha(cadena), que devuelve un objeto fecha
construido con la fecha y hora indicada en la cadena que debe tener
formato DD/MM/AAAA 1 hh:mm:ss."""

class fecha:
    def __init__(self):
        pass
    
    @classmethod
    def fecha_actual(cls):
        return datetime.now().strftime('%Y/%m/%d')

    @classmethod
    def hora_actual(cls):
        return datetime.now().strftime('%H:%M:%S')

    @classmethod
    def a_cadena(cls):
        return datetime.now().strftime('%d/%m/%y - %H:%M:%S')

"""Utilizando las facilidades que ofrece Python en relación al paradigma
funcional, programe las siguientes funciones:
• Una función que filtre una lista de elementos de acuerdo a una función
de verdad que reciba como argumento.
• Una función que devuelva la división de una lista de elementos
suministrada como argumento."""

if __name__ == '__main__':
    x = lambda x: x % 3 == 0
    f = filter(x, [3, 45, 6, 8, 66, 15])
    for i in f:
        print(i)
    yy = lambda x,y: x/y
    ff = map(yy, [4,2,8],[2,2,7])
    for i in ff:
        print(i)
    """martin_cuenta = cuenta_bancaria('martin', 18, 0)
    martin_cuenta.depositar(1000)
    cuenta_bancaria.mostrar(martin_cuenta)
    martin_cuenta.extraer_dinero(700)
    cuenta_bancaria.mostrar(martin_cuenta)

    raul_cuenta = cuenta_bancaria('raul', 45, 100)
    print('transferencia')
    cuenta_bancaria.transferir(martin_cuenta, 150, raul_cuenta)
    cuenta_bancaria.mostrar(martin_cuenta, raul_cuenta)

    raul_cuenta.extraer_todo()
    cuenta_bancaria.mostrar(raul_cuenta)"""

    #print(fecha.a_cadena())

