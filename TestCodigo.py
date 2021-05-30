import OperacionesAritmeticas


def menu():
   print("__MENU_______________")
   print("__1.Suma_____________")
   print("__2.Resta____________")
   print("__3.Multiplicación___")
   print("__4.División_________")
   print("__5.Salir____________")
   op=int(input())
   return op

   


#---------Inicia programa-----------------


opcion=1

while opcion>=1 and opcion<5 :
      valor1=float(input("Ingrese el valor1:"))
      valor2=float(input("Ingrese el valor2:"))
      opcion=menu()
      if opcion==1 :
         print ("Rta de la suma es:",OperacionesAritmeticas.suma(valor1,valor2))
      if opcion==2 :
          print ("Rta de la resta es:",OperacionesAritmeticas.resta(valor1,valor2))
      if opcion==3 :
         print ("Rta de la multiplicacion es:", OperacionesAritmeticas.multiplicacion(valor1,valor2))
      if opcion==4 :
          print ("Rta de la division es:",OperacionesAritmeticas.division(valor1,valor2))
 



