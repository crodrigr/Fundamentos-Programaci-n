

# archivo = open('datos_empleados.csv')
# for linea in archivo:
#     linea=linea.strip().split(';')
#     print(linea)
# archivo.close() 


# a = open('pruebaG44.txt', 'a')
# a.write('hola\n')
# a.write('mundo.\n')
# a.close()

archivo = open('alumno.txt','w')
alumno = ('Perico', 'Los Palotes', 90, 75, 38, 65)
linea = ':'.join(map(str, alumno)) + '\n'
archivo.write(linea)