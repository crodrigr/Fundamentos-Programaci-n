print("ARCHVOS TXT: LECTURA Y ESCRITURA")

datos=open('datos.txt')

for linea in datos: 
    print(linea)
datos.close()

info=open('test.csv')
for linea in info:
    x=linea.strip().split(';')
    print(x)
info.close()

