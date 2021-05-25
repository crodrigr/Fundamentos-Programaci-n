import random 

print("Ejercicios con listas")

#Variables globales
notas=[]
numEstudiantes=5

#Funcion que llena la lista con las notas de los estudiantes
def cargarNotas():
    for i in range(0,numEstudiantes) :
        notas.append(random.randint(0,5))

#Función que imprime la nota de los estudiantes
def imprimirNotas() :
    notas.sort()
    for i in range(0,numEstudiantes) :
        print("Estudiante: ",i," nota: ",notas[i])

def promedioNotas() :
    promedio=sum(notas)/numEstudiantes
    return promedio

def registraNota() :
    nota=int(input("Ingrese la nota del estudiante: "))
    global numEstudiantes
    numEstudiantes=numEstudiantes+1    
    notas.append(nota)

def menu() :
    print ("____MENU_____")
    print ("____1.Registrar Nota_____")
    print ("____2.Imprimir Notas_____")
    print ("____3.Promedio_____")
    print ("____4.Salir_____")
    return int(input())


#Inicia ejecución del programa
cargarNotas()
op=menu()
while op>=1 and op<4 :
    if op==1:
       registraNota()
       #numEstudiantes=numEstudiantes+1
    elif op==2:
        imprimirNotas()
        print(notas)
    elif op==3:
        print("El promedio de la notas es: ", promedioNotas())
    elif op==4:
       print ("Salir")
    op=menu()




input()