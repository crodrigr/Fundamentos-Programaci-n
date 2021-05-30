print("PARTIDO DE TENIS CON LISTAS")
import random
#--------Definición de funciones--------------#

#tenistas=['Nadal','Melzer','Murray','Soderling','Djokovic','Berdych','Federer','Ferrer']
tenistas=['Nadal','Melzer','Murray','Soderling','Djokovic','Berdych','Federer','Ferrer','Juan','Pedro','David','Eli','Willy','Jorge','Carlos','Daniel']#tenistas=[]


def crearTenista() :
    nombre=input("Ingrese el nombre del tenista: ")
    tenistas.append(nombre)   

def mostrarTenistas(li):
    for i in range(len(li)):
        print("Jugador ",i+1, ":", li[i])

def rondas(l1) :
    nuevaRonda=[]    
    for i in range(0,len(l1),2) :
         print ("a.",l1[i],"- b.",l1[i+1],": ",end='')
         g=random.randint(1,2)
         if (g==1) :
            print("a")
            nuevaRonda.append(l1[i])        
         else : 
            print("b")
            nuevaRonda.append(l1[i+1])            
    return nuevaRonda          



#--------Inicio de programa-------------------#
mostrarTenistas(tenistas)
print("")
while len(tenistas)>1  :
    tenistas=rondas(tenistas)
    print(" ") 
    mostrarTenistas(tenistas)
    print(" ")