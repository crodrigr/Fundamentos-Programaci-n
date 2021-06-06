

def palindroma(l):
    sw=True
    tl=len(l)
    if tl%2==0:
       hasta=int(tl/2)
    else:
       hasta=int((tl-1)/2)
    for i in range(hasta):
        if l[i]!=l[(tl-1)-i] :
           sw=False
           break
    return sw   

cadena=input("Ingrese una cadena: ")
cadena=list(cadena)
temp=list(cadena)
#print("La cadena es:", palindroma (cadena))
temp.reverse()
if cadena==temp :
    print("La cadena es:true")
else :
    print("La cadena es:false")