print("NUMERO COMBINATORIO")

#primer momento definicion de la función
def factorial(n) :
  f = 1
  for i in range(1, n + 1):
   f *= i 
  return f

def combinatoria(m,n):
    rta=0
    rta=factorial(m)/factorial(m-n)*factorial(n)
    return rta


m=int(input("Ingrese m: "))
n=int(input("Ingrese n: "))
#segundo momento llamado de la función. 
rta=combinatoria(m,n)

print ("Numero combinatorio: ",n," ",m, "es: ",rta)