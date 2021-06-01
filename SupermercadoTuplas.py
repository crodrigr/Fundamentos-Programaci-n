#Definicion de tuplas - bd
productos = [
    (41419, 'Fideos',        450, 210),
    (70717, 'Cuaderno',      900, 119),
    (78714, 'Jabon',         730, 708),
    (30877, 'Desodorante',  2190,  79),
    (47470, 'Yogur',          99, 832),
    (50809, 'Palta',         500,  55),
    (75466, 'Galletas',      235,   0),
    (33692, 'Bebida',        700,  20),
    (89148, 'Arroz',         900, 121),
    (66194, 'Lapiz',         120, 900),
    (15982, 'Vuvuzela',    12990,  40),
    (41235, 'Chocolate',    3099,  48),
]

clientes = [
    ('11652624-7', 'Perico Los Palotes'),
    ( '8830268-0', 'Leonardo Farkas'),
    ( '7547896-8', 'Fulanita de Tal'),
]

ventas = [
    (1, (2010,  9, 12),  '8830268-0'),
    (2, (2010,  9, 19), '11652624-7'),
    (3, (2010,  9, 30),  '7547896-8'),
    (4, (2010, 10,  1),  '8830268-0'),
    (5, (2010, 10, 13),  '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

def producto_mas_caro(productos) :
     precioMayor=productos[0][2]
     posicion=0
     for i in range(1,len(productos)) :
        if(precioMayor < productos[i][2]) :
           precioMayor=productos[i][2]
           posicion=i
     return posicion

def valor_total_bodega(p):
    valorTotal=0
    for i in range(len(p)) :
         valorTotal+=p[i][2]*p[i][3]                    
    return valorTotal


print("El producto mas costoso es:", productos[producto_mas_caro(productos)][1],"precio: " ,productos[producto_mas_caro(productos)][2] )
print("El valor total de la bodega es:", valor_total_bodega(productos) )