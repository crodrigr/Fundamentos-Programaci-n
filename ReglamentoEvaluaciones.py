import random
print("REGLAMENTO DE EVALUACIONES LA U. SANTA MARTA")

#---------Definicion de funciones----------------------#

aprobados=0
reprobados=0

def getNota():
 return random.randint(0,10)
     
def getNotasCertame() :
    xaprobado=0
    xreprobado=0
    global aprobados
    global reprobados
    c1=getNota()
    c2=getNota()
    print("C1: ",c1)
    print("C2: ",c2)
    if (  c1<2 and c2<2 ) :
        print ("Reprobado")
        reprobados+=1 #reprobado=reprobado+1
        xreprobado+=1
        
    elif ( c1>9 and c2>9 ) :
        print ("Aprobado")
        aprobados+=1
        xaprobado+=1
    else :
        c3=getNota()
        print("C3: ",c3)     
        promedio=(c1+c2+c3)/3
        if ( promedio < 3  ) :
          print ("Reprobado")
          reprobados+=1
          xreprobado+=1
        elif ( promedio < 7) :
          ex=getNota() 
          print("EX: ",ex)
          if(ex>=5): 
             print ("Aprobado")
             aprobados+=1
             xaprobado+=1
          else:
             print ("Reprobado")
             reprobados+=1
             xreprobado+=1
        else :
           print ("Aprobado")
           aprobados+=1 
           xaprobado+=1
    return  xaprobado,xreprobado 


#---------Inicio programa----------------------#

numEstudiantes=int(input("Ingrese el número de estudiantes a evaluar: "))

apro=0
repro=0
for i in range(numEstudiantes):
    print("Notas del estudiante: ",i+1)
    g,d=getNotasCertame()
    apro=apro+g
    repro=repro+d
    print("--------------------------")
print("Resultados finales ")
print("Total de aprobados:  ", aprobados)
print("Total de reprobados: ", reprobados)
print("Total de aprobados apro:  ", apro)
print("Total de reprobados repro:  ", repro)
