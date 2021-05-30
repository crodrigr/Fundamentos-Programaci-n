print("LISTA MAYORES QUE")

def mayores_que(x,lista) :
    contador=0
    for i in range(len(lista)) :
        if x<lista[i] :
             contador=contador+1    
    return contador 

a=5
l=[5,6,9,0,3,5,3,8,7]

print ("Mayores de ",a, "son: ",mayores_que(a,l))    