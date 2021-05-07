# coding: utf-8
# Your code here!

numRegistro=0

partidos = {1: {'Fecha': '25/03/2021', 'Nombre': 'Camilo Rodriguez','Eq. Rival': 'UIS', 'Goles Rival': 3, 'Goles Unab':4},
            2: {'Fecha': '28/03/2021', 'Nombre': 'Diana Taraza','Eq. Rival': 'UDI', 'Goles Rival': 3, 'Goles Unab':4},
			3: {'Fecha': '29/03/2021', 'Nombre': 'Juan Camargo','Eq. Rival': 'UDES', 'Goles Rival': 2, 'Goles Unab':4}           }

   

print ('PROGRAMA REGISTRO DE PARTIDOS')

def printMenu():
    print ("MENU PRINCIPAL")
    print ("1. Registrar partido")
    print ("2. Ver resultados")
    print ("3. Tabla de clasificacion")
    print ("4. Salir")
    rta = int(input())
    return rta
    
def addPartido():
    numRegistro+1
    op=1
    while op==1 :
       partido = {"Fecha":  input("Fecha: "),
                  "Nombre": input("Nombre: "),
                  "Eq. Rival": input("Equipo Rival: "),
                  "Goles Rival": int(input("Goles Rival: ")),
                  "Goles Unab": int(input("Goles Unab: "))}
       partidos[numRegistro]=partido
       op=int(input("Desea registra otro partido ingrese (0 o 1): 0.No 1.Si: "))

def  verResultados():      
 for p_id, p_info in partidos.items():
      print('Fecha:',p_info['Fecha'] + ' UNAB Goles (',p_info['Goles Unab'] , ') Rival Goles (', p_info['Goles Rival'], ') Equi: ', p_info['Eq. Rival'] )
         
         

def verClasificacion():
  partidosJugados=numRegistro
  partidosGanados=0
  partidosPerdidos=0
  partidosEmpatados=0
  puntosObtenidos=0
  for p_id, p_info in partidos.items():
      partidosJugados=partidosJugados+1
      if p_info['Goles Unab'] > p_info['Goles Rival']:
         partidosGanados=partidosGanados+1;
         print('Entro if ganados')
      elif p_info['Goles Unab'] == p_info['Goles Rival']:
           partidosEmpatados=partidosEmpatados+1 
      else:
           partidosPerdidos=partidosPerdidos+1
  puntosObtenidos=partidosGanados*3+partidosEmpatados
  print('Cantidad total de partidos Jugados por el equipo UNAB',partidosJugados)
  print('Cantidad total de partidos Ganados por el equipo UNAB',partidosGanados)
  print('Cantidad total de partidos Empatados por el equipo UNAB',partidosEmpatados)
  print('Cantidad total de partidos Perdidos por el equipo UNAB',partidosPerdidos)
  print('Total de puntos obtenidos por el equipo UNAB',puntosObtenidos)

         
       

def menu():
    op=printMenu()
    while op > -1 and op <4 :
          if op == 1:
	          addPartido()
          elif op == 2:
	          verResultados()
          elif op == 3:
	          verClasificacion()
          elif op == 4:
	          print('4. SALIR')      
          op=printMenu()
      
menu()  




    












    










