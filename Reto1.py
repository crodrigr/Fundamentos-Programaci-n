print("     CALCULAR NOTA QUE NECESITA\n ")

c1 =float(input(" - ingrese la nota del primer parcial: "))
c2 =float(input("\n - ingrese la nota del segundo parcial: "))
nl =float(input("\n - ingerse la nota de laboratorio: "))

nc=60-(nl*0.3)
ca=(c1+c2)
c3=((30*nc)-(7*ca))/7

print(("\n - Necesita Sacar"),c3,(" en el tercer parcial"))

input ()
