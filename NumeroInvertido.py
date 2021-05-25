
num=raw_input("Ingresar número:")
valor=int(num)
valor2=int(num[2])*100+int(num[1])*10+int(num[0])

i=len(num)-1
resultado=0
while i>=0 :
  resultado=resultado+((int(num[i])*(10**i)))
  i=i-1;

#resultado=valor+valor2
print "suma numeroriginal y el invertido", resultado