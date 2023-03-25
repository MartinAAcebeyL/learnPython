import os

class validacion_user(object):
    def minimo(self, contraseña):
        valor = True if (len(contraseña) >= 6 and len(contraseña) <= 12) else False
        return valor

    def alfanumerico(self, contraseña):
        valor = True if str(contraseña).isalnum() else "debe ser alfanumerico"
        return valor 

    def menos_6_caracteres(self, contraseña):
        valor = "debe tener mas de 6 caracteres" if len(contraseña) < 6 else True
        return valor 

    def mas_12_caracteres(self, contraseña):
        valor = "debe tener menos de 12 caracteres" if len(contraseña) > 12 else True
        return valor

    def validacion(self, contraseña):
        tupla = (self.minimo(contraseña),True)
        """,self.alfanumerico(contraseña)"""
        if tupla.count(True) == len(tupla):
            return True
        else:
            print("revise la contra validacion")   

class validacion_user1(object):
    def minimo(self, contraseña):
        valor = True if len(contraseña)>8 else "no es seguro"
        return valor

    def concretacion(self, contraseña):
        tupla = tuple(contraseña)
        lista = []
        for i in tupla:
            lista.append(ord(i))
        lista.sort()
        conjunto_valores = set(lista)
        conjunto_valores_numericos  = conjunto_valores.intersection(range(48,58))
        conjunto_valores_minusculas = conjunto_valores.intersection(range(97,123))
        conjunto_valores_mayusculas = conjunto_valores.intersection(range(65,91))
        conjunto_valores_no_alphanu = conjunto_valores.intersection(range(33,48))
        if len(conjunto_valores_numericos) > 0 and len(conjunto_valores_minusculas) > 0 and len(conjunto_valores_mayusculas) > 0 and len(conjunto_valores_no_alphanu) > 0:
            return True
        return False
    
    def espacios(self, contraseña):
        valor = True if str(contraseña).count(" ") == 0 else False
        return valor

    def validacion1(self, contraseña):
        tupla = (self.minimo(contraseña),
                self.concretacion(contraseña),
                self.espacios(contraseña))
        
        if tupla.count(True) == len(tupla):
            return True
        else:
            print("revise la contra validacion1")

class validacion(validacion_user, validacion_user1):
    def validacion_contrasena(self, contraseña, user):
        tupla = (self.validacion(contraseña),
                self.validacion1(contraseña))

        if tupla.count(True) == len(tupla):
            return True
        else:
            print("revise la contra validacion_contra")

def function():      
    while(True):
        valor = validacion()
        contra = str(input("de la contra "))
        resul = valor.validacion_contrasena(contra, "martin")
        if resul == True:
            print("bienvenido")
            break
        os.system("cls")