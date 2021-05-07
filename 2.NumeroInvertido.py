a = int(raw_input('Ingrese a: '))

b=a%10
r=b*100
print 'r',r
a=int(a/10)
print 'a',a
b=a%10
print 'b',b
r=r+b*10
print 'r',r
a=int(a/10)
r=r+a
print 'Invertido',r

