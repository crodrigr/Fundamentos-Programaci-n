import LibreriaListas

print("LISTA MAYORES QUE EL PROMEDIO")

#Inicia programa
tl=int(input("Ingrese el número de datos a solicitar: "))    
lista=[]
lista=LibreriaListas.llenarLista(tl,lista)
mayoresPromedio=LibreriaListas.cuantosMayoresPromedio(lista)
print("Mayores de promedio son:",mayoresPromedio)
lista2=[3,4,5,6,7,8,9,10]
mayoresPromedio2=LibreriaListas.cuantosMayoresPromedio(lista2)
print("Mayores de promedio son:",mayoresPromedio2)
