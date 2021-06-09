# Leer y escribir en formato JSON
import json

datos={
    'nombre':'Camilo',
    'apellido':'Rodriguez',
    'email':'crodrigr@gmail.com',
    'edad':38,
    'pais':'Colombia'
}

#recibe un diccionario y transforma a formato JSON

cadena_json=json.dumps(datos)
print(datos)

#Escritura
with open('datos.json','w') as f:
    json.dump(datos,f)

#Lectura
with open('datos.json','r') as f:
    cadena_json=json.load(f)

    print(cadena_json)

