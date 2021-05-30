import random
print ("USO DEL RANDOM")

#----------Definición de funciones---------

def getNumeroDado(): 
   print (format(random.uniform(0.0,10)))
   return random.randint(1,6)
    
def getLanzamiento() :
    d1=getNumeroDado()
    d2=getNumeroDado()
    rta=d1+d2
    return rta



#---------Inicia programa-------------------

j1=getLanzamiento()
j2=getLanzamiento()
j3=getLanzamiento()

print("Resultados: j1:",j1, " j2: ",j2," j3:",j3)

if j1>j2 and j1>j3:
   print ("El ganador es j1:",j1)
if j2>j1 and j2>j3:
   print ("El ganador es j2:",j2)
if j3>j1 and j3>j2:
    print ("El ganador es j3:",j3) 
