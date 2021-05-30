def es_par(n):
    return n % 2 == 0

def es_impar(n):
    return not es_par(n)

def pares_hasta(n):
    return range(0, n, 2)