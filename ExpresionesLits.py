a = [5, 1, 4, 9, 0]
#   [0, 1, 4, 5, 9]
#b = [range(3, 10)] + [range(20, 23)]
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato', 'jirafa', 'elefante']
e = ['a', a, 2 * a]

print(a[2])
print(c[1][2])
print(e[0] == e[1])
print(len(c[0]))
print(c[-1])
print(c[-1][+1])
print(c[2:] + d[2:])
print(a[3:10:2])
print(d.index('jirafa'))
print(sorted(a)[2])
print(e)
print(e[c[0][1]].count(8))
