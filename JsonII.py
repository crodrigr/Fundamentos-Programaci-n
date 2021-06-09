# Leer y escribir en formato JSON
import json
import pickle

datos={}
datos['programadores']=[]

a={ 'Id':1001,
    'nombre':'Camilo',
    'apellido':'Rodriguez',
    'email':'crodrigr@gmail.com',
    'edad':38,
    'pais':'Colombia'
}

b={ 'Id':1002,
    'nombre':'Andres',
    'apellido':'Martinez',
    'email':'amarir@gmail.com',
    'edad':48,
    'pais':'Colombia'
}

c={ 'Id':1003,
    'nombre':'Milton',
    'apellido':'Oyola',
    'email':'moyola@gmail.com',
    'edad':28,
    'pais':'Colombia'
}

datos['programadores'].append(a)
datos['programadores'].append(b)
datos['programadores'].append(c)


#recibe un diccionario y transforma a formato JSON

cadena_json=json.dumps(datos)
print(datos)

#Escritura
with open('programadores.json','w') as f:
    json.dump(datos,f)

#Lectura
with open('programadores.json','r') as f:
    cadena_json=json.load(f)


for p in cadena_json['programadores'] :
    print('Id:  %i' % p['Id'])
    print('Nombre:  %s' % p['nombre'])
    print('Apellido:  %s' % p['apellido'])
    print('edad:  %s' % p['email'])
    print('pais:  %s' % p['pais'])
    print()

#Persistencia en un archivo binario:
with open('programadoresBinario.pkl','wb') as f:
    pickle.dump(datos,f,protocol=pickle.HIGHEST_PROTOCOL)
    

#Lectura de un archivo binario
with open('programadoresBinario.pkl','rb') as f:
    datos_deserializados = pickle.load(f)

print(type(datos_deserializados))
print(datos_deserializados)

for p in datos_deserializados['programadores'] :
    print('Id:  %i' % p['Id'])
    print('Nombre:  %s' % p['nombre'])
    print('Apellido:  %s' % p['apellido'])
    print('edad:  %s' % p['email'])
    print('pais:  %s' % p['pais'])
    print()