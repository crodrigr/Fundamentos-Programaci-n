#------Definicion de funciones--------------#
import random
print("PROMEDIO DE NOTAS USANDO LISTAS")

notas=[]

def cargarNotas(numEstudiantes):
    for i in range(numEstudiantes) :
        notas.append(random.randint(0,5))

def mostrarNotas():
    for i in range(len(notas)):
        print("Estudiante ",i,"nota: ",notas[i])

def cantidadxNota():
    print("Nota 0:",notas.count(0))
    print("Nota 1:",notas.count(1))
    print("Nota 2:",notas.count(2))
    print("Nota 3:",notas.count(3))
    print("Nota 4:",notas.count(4))
    print("Nota 5:",notas.count(5))

def promedioNotas():
    return sum(notas)/len(notas)



#------Inicio de programa-------------------#
numEstu=int(input("Ingrese el número de estudiantes: "))
cargarNotas(numEstu)
notas.sort()
mostrarNotas()
print("Total suma notas ",sum(notas))
print("")
print("El promedio es: ",promedioNotas())
print("")
cantidadxNota()
