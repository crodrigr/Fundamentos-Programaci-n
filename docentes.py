
dato_docentes={}
dato_docentes['docentes']=[]

a={
    'Id:' :1,
    'nombres':'Camilo',
    'apellidos': 'Rodriguez',
    'telefono' : '31254890',
    'direccion':'Calle 34 No- 56',
    'tituloProfesional': 'Ingeniero de Sistemas',
    'nivelEstudios':'Maestria'
}

dato_docentes['docentes'].append(a)



def menuDocente():
    print("__MENU DOCENTE___")
    print("__1.Crear docente___")
    print("__2.Buscar docente___")
    print("__3.Eliminar docente___")
    print("__4.Salir___")
    op=int(input())
    return op