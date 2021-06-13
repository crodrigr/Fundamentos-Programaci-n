
#Definicion de funciones y variables globales
import json
import os

datos={}
datos['programadores']=[]

def crearProgramados() :
    programador={}
    Id=int(input("Ingrese id:"))
    nombre=input("Ingrese nombre:")
    apellido=input("Ingrese apellido:")
    email=input("Ingrese email:")
    edad=int(input("Ingrese edad:"))
    pais=input("Ingrese pais:")
    programador['Id']=Id    
    programador['nombre']=nombre    
    programador['apellido']=apellido    
    programador['email']=email    
    programador['edad']=edad    
    programador['pais']=pais  
    datos['programadores'].append(programador)

def guardarJson():
    with open('programadores.json','w') as f:
      json.dump(datos,f)

def loadJson():
    with open('programadores.json','r') as f:
     global datos
     datos=json.load(f)

    
def listarProgramador() :
    for p in datos['programadores'] :
        print('Id:  %i' % p['Id'])
        print('Nombre:  %s' % p['nombre'])
        print('Apellido:  %s' % p['apellido'])
        print('Email:  %s' % p['email'])
        print('Edad:  %s' % p['edad'])
        print('pais:  %s' % p['pais'])
        print()
    


def mostraProgramdores() :
    print(datos)


def menuPrincipal():
    #os.system ("cls") 
    print("___MENU PRINCIPAL____________")
    print("___1.Crear programador_______")
    print("___2.Listar programdores_____")
    print("___3.Guardar___")
    print("___4.Salir___________________")
    return int(input())


#Inicio programa principal
loadJson()
op=menuPrincipal()

while op>0 and op<4 :
   if  op==1:
        crearProgramados()        
   elif op==2:
       listarProgramador()
   elif op==3:       
       guardarJson()   
   op=menuPrincipal()
   