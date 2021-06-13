'''
telefonos = { 
              'Pepito': 5552437, 
              'Jaimito': 5551428, 
              'Yayita': 5550012
             }

telefonos['camilo']=5487785

for k in telefonos:
   print(k)

for k in telefonos.values():
   print(k)

for k, v in telefonos.items():
    print ('El telefono de', k, 'es', v)

print(list(telefonos.items()))

if 'camilo' in telefonos :
    print("Si esta la llave camilo")
else :
    print("No esta la llave camilo")'''


d = {
  (1, 2): [{1, 2}, {3}, {1, 3}],
  (2, 1): [{3}, {1, 2}, {1, 2, 3}],
  (2, 2): [{}, {2, 3}, {1, 3},{3,4}],
}
a=[]
c=3
print(type(c))

