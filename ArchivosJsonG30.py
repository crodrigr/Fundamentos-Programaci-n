import json

datos={
    'nombre':'Camilo',
    'apellido':'Rodriguez',
    'email':'crodrig@gmail.com'
}

#cadena_json=json.dumps(datos)
#print(cadena_json)
'''
with open('datos.json','w') as f:
    json.dump(datos,f)'''

with open('datos.json','r') as f:
     cadena_json=json.load(f)
    
print(cadena_json)