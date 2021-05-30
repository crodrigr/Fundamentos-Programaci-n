def tamanoCadena(x) :
    return len(x)

animales = ['conejo', 'ornitorrinco', 'pez', 'hipopotamo', 'tigre']

animales.sort(key=tamanoCadena)

print(animales)