# 1) Carga de Datos:
# Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
# «fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
# «producto»: una cadena de texto que represente el nombre del producto vendido.
# «cantidad»: un número entero que represente la cantidad de productos vendidos.
# «precio»: un número flotante que represente el precio unitario del producto.

ventas = [
    {'fecha': '2024-01-01', 'producto': 'remera', 'cantidad': '2', 'precio': '2000'},
    {'fecha': '2024-01-02', 'producto': 'pantalon', 'cantidad': '3', 'precio': '3000'},
    {'fecha': '2024-01-03', 'producto': 'campera', 'cantidad': '4', 'precio': '4000'}
]

#2) Cálculo de Ingresos Totales:
# Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.

# total = 0
# for i in range(len(ventas)):
#     sub_total = int(ventas[i]['cantidad']) * int(ventas[i]['precio'])
#     total += sub_total
# print(f'Total: {total}')


#3) Análisis del Producto Más Vendido:
# Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
# Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.

ventas_por_producto = {
    "remera": 10,
    "pantalon": 25,
    "camisa": 2
}

# mayor_prod = max(ventas_por_producto, key=ventas_por_producto.values.get)
# mayor_cant = max(ventas_por_producto.values())
# print(f'Mayor prodcto vendido: {mayor_prod}, cantidad: {mayor_cant}')

#4) Promedio de Precio por Producto:
# Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
# Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.

precios_por_producto = {
    "botella": (1200, 6),
    "mouse": (2000, 2),
    "silla": (9000, 3)
}

# promedio = 0
# for clave, tupla in precios_por_producto.items():
#     i = 0
#     promedio = tupla[i] / tupla[i + 1]
#     print(f'El producto: {clave}, total y cantidad: {tupla}, promedio: {promedio}')

#5) Ventas por Día:
# Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
# Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.

ingresos_por_dia = [
    ("13-02-2026", 10000),
    ("13-02-2026", 20000),
    ("14-02-2026", 5000),
]

# ingresos_totales_por_día = {}

# for fecha, total in ingresos_por_dia:
#     if fecha in ingresos_totales_por_día:
#         ingresos_totales_por_día[fecha] += total
#     else:
#         ingresos_totales_por_día[fecha] = total
# print(f'{ingresos_totales_por_día}')

#6) Representación de Datos:
# Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
# «cantidad_total»: la cantidad total vendida del producto.
# «ingresos_totales»: los ingresos totales generados por la venta del producto.
# «precio_promedio»: el precio promedio de venta del producto.

# resumen_ventas = {
#     'auto': {
#         'cantidad_total': 10,
#         'ingresos_totales': 10000,
#         'precio_promedio': 1000
#     },
#     'camioneta': {
#         'cantidad_total': 5,
#         'ingresos_totales': 10000,
#         'precio_promedio': 2000
#     },
#     'moto': {
#         'cantidad_total': 10,
#         'ingresos_totales': 5000,
#         'precio_promedio': 500
#     },
# }

# for prod, ventas in resumen_ventas.items():
#     print(f'Se vendio: {prod}, cantidad total: {ventas['cantidad_total']}, ingresos totales: {ventas['ingresos_totales']}, precios x/u: {ventas['precio_promedio']}')
