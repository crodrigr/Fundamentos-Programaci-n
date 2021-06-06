
def mayores_que(x,lista):
    c=0
    for i in lista:
       if x<i :
         c+=1
    return c


m=int(input("ingrese número mayor que"))
valores=[2,3,4,59,55,2,3,9,0,-1]
rta=mayores_que(m,valores)
print(valores)
print("Mayores que:",m," son:",rta)
