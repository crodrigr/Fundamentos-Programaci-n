valor = ['piedra', 'papel','tijera']
#informamos la variabe que quiere indicar el cliente
print("ingrese el valor piedra(0),papel(1),tijera(2)")
#Creamos el contador para las vecece ganadas
ganador = [0, 0]
JUEGOS = 0
#ingresamos la cantidad de juego
ju=int(input("ingrese la cantidad de juegos: "))
while JUEGOS <= ju:
# piedra(0), papel(1), tijeras(2)
    a = int(input("ingrese el valor a elegir jugador A: "))
    b = int(input("ingrese el valor a elegir jugador B: "))
    print ("El usuario A eligio: ", valor[a])
    print ("El usuario B eligio: ", valor[b])

    if a == b :
        print ("jugo empatado")
    elif a ==0 and b == 1 :
        print("Gana jugador B, Tijeras ganan a papel")
        ganador[1] +=1
    elif a ==0 and b == 2 :
        ganador[0] +=1
        print("Gana jugador A, Piedra le gana a tijeras")
    elif a ==1 and b == 0 :
        ganador[0] +=1
        print ("Gana jugador A, Papel le gana a piedra")
    elif a ==1 and b == 2:
        ganador[0] +=1
        print ("Gana jugador B, Tijeras de gana a piedra")
    elif a==2 and b== 0:
        ganador[1] +=1
        print ("Gana jugador B, Piedra le gana a tijera")
    elif a==2 and b== 1:
        ganador[0] +=1
        print ("Gana jugador A, tijera le gana a papel")
    print(ganador)
    JUEGOS = JUEGOS + 1
    #depender de la cantidad de juegos si ya se gano 3 veces indica el ganador
    if ganador[1] == 3:
        print("jugador B es el ganador")
        quit()
    elif ganador[0] == 3:
        print("jugador A es el ganador")
        quit()