alumnos = [
    ('Perico', 'Los Palotes', '201199001-5', 'Civil'),
    ('Fulano', 'De Tal',      '201199002-6', 'Electrica'),
    ('Fulano', 'De Tal',      '201199003-7', 'Mecanica'),
]

def mostraDatosPerson(nombres,apellidos,id,profesion) :
    print("Nombres: ",nombres)
    print("Apellidos: ",apellidos)
    print("Id: ", id)
    print("Profesion: ",profesion)
    

for i in range(len(alumnos)):
    nombre,apellido,id,profesion=alumnos[i]
    mostraDatosPerson(nombre,apellido,id,profesion)
    print(" ")

tem=(10,)
print("tamaño tupla: ",len(tem))

