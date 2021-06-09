import docentes
import json
import pickle

def loadData():
    with open('docentes.pkl','rb') as f:
     docentes.dato_docentes = pickle.load(f)

def guardar():
 with open('docentes.pkl','wb') as f:
    pickle.dump(docentes.dato_docentes,f,protocol=pickle.HIGHEST_PROTOCOL)
 with open('estudiantes.pkl','wb') as f:
    pickle.dump(docentes.dato_docentes,f,protocol=pickle.HIGHEST_PROTOCOL)
 with open('cursos.pkl','wb') as f:
    pickle.dump(docentes.dato_docentes,f,protocol=pickle.HIGHEST_PROTOCOL)
 with open('matriculas.pkl','wb') as f:
    pickle.dump(docentes.dato_docentes,f,protocol=pickle.HIGHEST_PROTOCOL)



def menu():
    print("__MENU DOCENTE___")
    print("__1.Docente___")
    print("__2.Estudiante___")
    print("__3.Curso___")
    print("__4.Matricula___")
    print("__5.Reportes___")
    print("__6.Salir___")    
    op=int(input())
    return op

#Inicio program

loadData()
op=menu()
while op>=1 and op<4 :
    if op==1:
       docentes.menuDocente()
    elif op==2:
       print("Estudiante")
    elif op==3:
       print("Curso") 
    elif op==4:
       print("Matricula") 
    elif op==5:
       print("Reportes") 
    elif op==6:
       guardar() 
    else :
       print ("Salir")
    op=menu()

