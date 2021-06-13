#Creado por Richard Andrés Villamizar Cano - Programa MinTIC - UNAB
#+++ RETO 2 - Python 3.9.5 +++

def validarJugada(jugada):
    if(jugada=='piedra' or jugada=='papel' or jugada=='tijera'):
        return True
    else:
        return False  
def aguardarJugada(jugador):
    jugadaFlag=False
    while(jugadaFlag==False):
        jugada = input(str(jugador)+': ')
        if(validarJugada(jugada)==True):
            jugadaFlag=True
            return jugada
        else:
            print (str(jugador)+' ingrese una jugada válida!')
def ganadorRonda(jugadaA, jugadaB):
    if((jugadaA=='tijera' and jugadaB=='papel') or (jugadaA=='papel' and jugadaB=='piedra') or (jugadaA=='piedra' and jugadaB=='tijera')):
        return 'A'
    elif ((jugadaB=='tijera' and jugadaA=='papel') or (jugadaB=='papel' and jugadaA=='piedra') or (jugadaB=='piedra' and jugadaA=='tijera')):
        return 'B'

print ('++ CACHIPUN ++')
rGanadasA=0
rGanadasB=0
flagNDias=False
while (rGanadasA!=3 and rGanadasB!=3):
    jugadaA=aguardarJugada('A')
    jugadaB=aguardarJugada('B')
    if(ganadorRonda(jugadaA, jugadaB)=='A'):
        rGanadasA+=1
    elif(ganadorRonda(jugadaA, jugadaB)=='B'):
        rGanadasB+=1
    print(str(rGanadasA)+' - '+str(rGanadasB)+'\n')
if(rGanadasA==3):
    print('A es el ganador')
elif (rGanadasB==3):
    print('B es el ganador')

