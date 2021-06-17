#valores
A=270
B=340
C=390
monedas=[]
print("A - 270\nB - 340\nC - 390")
#ingreso de datos
print("escoja uno de los tres productos:")
p=input()
if p== 'A' or p== 'a':
    print("Costo del Producto: ",A)
    costo=270
elif p== 'B' or p=='b':
    print("Costo del Producto:",B)
    costo=340
elif p== 'C'or p=='C':
    print("Costo del Producto:",C)
    costo=390
else:
    print("producto no existente")
#funcion ingreso monedas
print ("¿CUANTAS MONEDAS TRAE?")
mt=int(input())
IngresoMonedas=0
def monedasIngresadas():
    global IngresoMonedas
    for i in range(0,mt):
        print ('monedas aceptadas')
        print ('1. - $100 \n2. - $50 \n3. - $10')
        m=int(input("ingrese las monedas "))
        monedas.append(m)
        if m == 1:
            IngresoMonedas += 100
            monedas.append(100)
        elif m == 2:
            IngresoMonedas += 50
            monedas.append(50)
        elif m ==3: 
            IngresoMonedas += 10
            monedas.append(10)
        else:
            print ('Moneda no encontrado')
monedasIngresadas()
print ("sus monedas suman: ",IngresoMonedas)
print ("Sus Monedas Ingresadas son: ",monedas)
print ('Precio del Producto: ',costo)
#funcion registro de vueltos
vueltos= IngresoMonedas - costo
def vueltas():
    print ('sus vuelt0s son:',vueltos)
    vueltos100=int(vueltos/100)
    for i in range (vueltos100):
        print('100 ')
    vueltos50=int((vueltos-(vueltos100*100))/50)
    for i in range (vueltos50):
        print('50 ')
    vueltos10=int((vueltos-(vueltos100*100)-(vueltos50*50))/10)
    for i in range (vueltos10):
       print('10')
vueltas()


