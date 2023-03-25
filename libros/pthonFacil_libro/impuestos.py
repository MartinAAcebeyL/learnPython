fob=float(input('de el precio del producto '))

cif=fob+5+(fob*0.02)

ga=5
#float(input('de el ga% '))
iva = 0.1494

GA = cif *(ga/100)
IVA = (cif + GA) * iva

#print(str(GA)+' '+str(IVA))
IMPUESTOS = GA + IVA
print(IMPUESTOS)