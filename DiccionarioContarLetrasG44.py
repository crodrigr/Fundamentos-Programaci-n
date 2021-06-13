

def contar_inciales(oracion):    
    diccionario = dict()
    oracion=oracion.lower() 
    letra=oracion[0]  
    for i in range(len(oracion)):
        ctador=0
        if(i-1>0 and i!=0) : 
         if(oracion[i-1]==" ") :
             letra==oracion[i-1]                 
         for j in range(i,len(oracion)):            
             if(j-1>0) : 
                if(oracion[j-1]==" ") :
                    if(letra==oracion[j-1]):
                            ctador+=1
        diccionario[letra]=ctador
    print(diccionario) 
 


    return diccionario

def contar_letras(oracion,listkeys):    
    diccionario = dict()
    oracion=oracion.lower()
    listkeys=listkeys.lower()    
    for caracter in range(len(listkeys)):

        if(listkeys[caracter] in oracion):
            diccionario[listkeys[caracter]] = oracion.count(listkeys[caracter])

    return diccionario


rta=contar_inciales(input("Ingrese la oración iniciales: "))

'''
abecedario = "abcdefghijklmnopqrstuvxyz"
vocales="aeiou"

rta=contar_letras(input("Ingrese la oración abecedario: "),abecedario)
print("Abecedario")
print(rta)
rta=contar_letras(input("Ingrese la oración vocales: "),vocales)
print("Vocales")
print(rta) '''

'''
def validar(frase):
  diccionario={}
  cadena=list(dict.fromkeys(frase))
  for i in range(len(cadena)):
    if str(cadena[i])!=" ":
      diccionario[str(cadena[i])]=frase.count(cadena[i])
  return diccionario


frase=input("frase: ")
print(validar(frase))'''