print (" -------------")

#------Definición de funciones y variables globales-----------------#

#Variables globales

hasta=4

def getCombinacionNumeros() :
    global hasta
    hasta=hasta-1
    contador=0
    for i in range(1,hasta+2) :
        for j in range(1,hasta+2) :            
            print(i,j)
            contador+=1
        print(" ")
    print("contador ",contador)
   

#------Inicio de programa-------------------------------------------#
contador=0
# Llamado 1
getCombinacionNumeros()
contador+=1
print("---------------")
# Llamado 2
getCombinacionNumeros()
contador+=1
print("---------------")
# Llamado 3
getCombinacionNumeros()
contador+=1
print("hasta",hasta)
print("contador",contador)