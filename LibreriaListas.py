def cuantosMayoresPromedio(l) :
    promedio=sum(l)/len(l)
    print("Promedio es:",promedio)
    contador=0
    for i in range(len(l)) :
        if l[i]>promedio:
            contador=contador+1
    return contador

def llenarLista(t,l) :
    for i in range(t):
        dato=int(input ("Ingresar dato: "))
        l.append(dato)
    return l