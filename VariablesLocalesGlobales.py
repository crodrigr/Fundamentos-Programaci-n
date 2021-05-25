
#Variables globales
z=4
x=5
respuestaResta=0

def suma(): 
  z=10
  z=z+5
  respuesta=z+x 
  return respuesta

def resta(q,w):  
   respuestaResta=q-w
   print (respuestaResta)


#Inicio de programa
print("El resultado de la suma es:",suma())
print("El resultado de la resta es:",resta(10,5),respuestaResta)
print("El resultado de la resta es:",resta(40,5),respuestaResta)



input()