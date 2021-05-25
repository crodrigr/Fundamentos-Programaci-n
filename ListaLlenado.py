

def llenarLista(t) :
    numeros=[]
    for i in range(0,t) :
        numeros.append(i)
    return numeros

    
def mostrarLista(numeros):
   for i in range(0,len(numeros)) :
        print (numeros[i])  


x=llenarLista(15)
mostrarLista(x)
print("----------------")
x=llenarLista(25)
mostrarLista(x)
print("----------------")
x=llenarLista(10)
mostrarLista(x)
