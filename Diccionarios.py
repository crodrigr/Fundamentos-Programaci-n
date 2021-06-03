
def contar_letras(cadena):
    caracteres={}    
    for i in range(len(cadena)):
         contador=0
         letra=cadena[i].lower()
         if letra!=' ' :
           for j in range(len(cadena)):
             if letra==cadena[j].lower():
                contador+=1  
             caracteres[letra]=contador
    return caracteres          
            



c="El elefante avanza hacia Asia"
d=contar_letras(c)
print(c)
print(d)
