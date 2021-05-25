print("PROGRAMA QUE DIBUJA UN CUADRADO")

#Entrada de datos
altura=int(input("Ingrese la altura: "))
ancho=int(input("Ingrese el ancho:")) 

#Proceso
'''
for i in range(0,altura) :
    for j in range(0,ancho) :
        if (i==0 or i==altura-1) :
           print("*",end='' )
        elif (j==0 or j==ancho-1) :
             print("*",end='' )
        else :
            print(" ",end='') 
    print()'''
i=2
n=20

while i<n :
      print(i)
      i=i+2
    


input()