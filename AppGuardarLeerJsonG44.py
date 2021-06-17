import json
#Variables globales
datos={}
datos['programadores']=[]


def crearProgramador() :
    programador={}
    nombres=input("Ingrese los nombres:")
    apellidos=input("Ingrese los apellidos:")
    email=input("Ingrese el email:")
    edad=int(input("Ingrese la edad:"))
    pais=input("Ingrese el pais:")
    programador['nombre']=nombres
    programador['apellido']=apellidos
    programador['email']=email
    programador['edad']=edad
    programador['pais']=pais
    programador['estado']=1
    global datos
    datos['programadores'].append(programador)
    guardar()

def mostrarProgramadores() :
    print("")
    print("------------------------------------------")
    for i in range(len(datos['programadores'])) :
      if datos['programadores'][i]['estado']==1 :
        print("Nombre: ",datos['programadores'][i]['nombre'])
        print("Apellido: ",datos['programadores'][i]['apellido'])
        print("Email: ",datos['programadores'][i]['email'])
        print("Edad: ",datos['programadores'][i]['edad'])
        print("Pais: ",datos['programadores'][i]['pais'])
        print("------------------------------------------")
    print("")

    
def menu() :
   print("___MENU PRINCIPAL_____________") 
   print("___1. Crear programador_______") 
   print("___2. Mostrar programadores___") 
   print("___3. Guardar_________________")
   print("___4. Eliminar________________") 
   print("___5. Buscar___________________")
   print("___6. Salir___________________")
   op=int(input())
   return op

def guardar() :
    with open('programadores_g44.json','w') as f:
     json.dump(datos,f)

    
def loadData() :
 try:
    with open('programadores_g44.json','r') as f:
     global datos
     datos=json.load(f)
 except IOError:
    print(" ")

def buscar(nombre):
     for i in range(len(datos['programadores'])) :
       if nombre in datos['programadores'][i]['nombre'] :
           return i
     return -1



#Inicio programa
loadData()
op=menu()
while op>=1 and op<6 :
    if op==1:
       print("")
       print("Crear programador")
       crearProgramador()
    elif op==2 :
       print("")
       print("Mostrar programadores")
       mostrarProgramadores()
    elif op==3 :
       print("Guardar")
       guardar()
    elif op==4 :
       print("Eliminar")
       nombre=input("ingrese nombre a buscar:")
       pos=buscar(nombre)
       if pos!=-1 :
          del(datos['programadores'][pos])
          #datos['programadores'][pos]['estado']=0
          guardar()
    elif op==5 :
       print("Buscar")
       nombre=input("ingrese nombre a buscar:")
       print(buscar(nombre))       
    op=menu()