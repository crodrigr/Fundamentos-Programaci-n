from math import sin, cos, tan

for i in range(1, 31):
    if i % 10 == 7:
        continue
    print (i, sin(i), cos(i), tan(i))

input()




