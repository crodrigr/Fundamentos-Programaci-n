import random
print("PARTIDOS DE TENIS")

#-------------------Definicion de funciones-----------------------#

#jugadores=['Nada','Melzer','Murray','Soderling','Djokovic','Berdych','Federer','Ferrer']
jugadores=['Nada','Melzer','Murray','Soderling','Djokovic','Berdych','Federer','Ferrer','Camilo','Pedro','Mario','Carlos','Jose','Silvio','Wilson','Daniel']

def mostrarJugadores(lj) :
    for i in range(len(lj)):
      print("Jugador ",i+1,lj[i])

def rondas(lj) :
  ganadores=[]
  for i in range(0,len(lj),2) : 
        print('a.',lj[i],"- b.",lj[i+1])
        ganador=random.randint(1,2)
        if(ganador==1):
           print("a")
           ganadores.append(lj[i])
        else:
          print("b")
          ganadores.append(lj[i+1])
  mostrarJugadores(jugadores)   
  if len(ganadores)>1:
     rondas(ganadores)
  else :
    print("")
    mostrarJugadores(jugadores) 

#-------------------Inicia programa-----------------------#

rondas(jugadores)

'''
while len(jugadores)>1  :
    print("")
    mostrarJugadores(jugadores)
    print("")
    jugadores=rondas(jugadores)
mostrarJugadores(jugadores)'''
