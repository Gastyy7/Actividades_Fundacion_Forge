#1) Carga de Datos:
# Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
# «fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
# «producto»: una cadena de texto que represente el nombre del producto vendido.
# «cantidad»: un número entero que represente la cantidad de productos vendidos.
# «precio»: un número flotante que represente el precio unitario del producto.

ventas = [
    {'fecha': '2024-01-01', 'producto': 'remera', 'cantidad': 7, 'precio': 2000},
    {'fecha': '2024-01-02', 'producto': 'pantalon', 'cantidad': 3, 'precio': 3000},
    {'fecha': '2024-01-03', 'producto': 'campera', 'cantidad': 2, 'precio': 4000},
    {'fecha': '2024-01-04', 'producto': 'zapatilla', 'cantidad': 10, 'precio': 1500},
    {'fecha': '2024-01-05', 'producto': 'media', 'cantidad': 9, 'precio': 500},
    {'fecha': '2024-01-06', 'producto': 'musculosa', 'cantidad': 5, 'precio': 1000}
]

#2) Cálculo de Ingresos Totales:
# Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.

# total = 0
# for i in range(len(ventas)):
#     sub_total = ventas[i]['cantidad'] * ventas[i]['precio']
#     total += sub_total
# print(f'Total: {total}')

#3) Análisis del Producto Más Vendido:
# Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
# Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.

# ventas_por_producto = {}

# for venta in ventas:
#     prod = venta["producto"]
#     cant = venta["cantidad"]
#     if prod in ventas_por_producto:
#         ventas_por_producto[prod] += cant
#     else:
#         ventas_por_producto[prod] = cant
# mayor_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
# canti_mayor_vendido = max(ventas_por_producto.values())
# print(f"Producto mas vendido: {mayor_vendido} Cantidad: {canti_mayor_vendido}")

#4) Promedio de Precio por Producto:
# Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
# Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.

# precios_por_producto = {}

# for venta in ventas:
#     prod = venta["producto"]
#     cant = venta["cantidad"]
#     precio = venta["precio"]
#     if prod not in precios_por_producto:
#         precios_por_producto[prod] = (0, 0)
#     suma_total, cantidad_total = precios_por_producto[prod]
#     precios_por_producto[prod] = (suma_total + precio * cant, cantidad_total + cant)

# print(precios_por_producto)

# for producto, (suma, cantidad) in precios_por_producto.items():
#     promedio = suma / cantidad
#     print(f"Producto: {producto}, promedio: {promedio}")

#5) Ventas por Día:
# Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
# Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.

# ingresos_por_dia = {}

# for venta in ventas:
#     fecha = venta["fecha"]
#     ingreso_total = venta["cantidad"] * venta["precio"]
#     if fecha in ingresos_por_dia:
#         ingresos_por_dia[fecha] += ingreso_total
#     else:
#         ingresos_por_dia[fecha] = ingreso_total
# print(ingresos_por_dia)
    
#6) Representación de Datos:
# Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
# «cantidad_total»: la cantidad total vendida del producto.
# «ingresos_totales»: los ingresos totales generados por la venta del producto.
# «precio_promedio»: el precio promedio de venta del producto.

resumen_ventas = {}

for venta in ventas:
    prod = venta["producto"]
    cant = venta["cantidad"]
    precio = venta["precio"]
    if prod not in resumen_ventas:
        resumen_ventas[prod] = {
            "cantidad_total": 0,
            "ingresos_totales": 0,
            "precio_promedio": 0
        }
    resumen_ventas[prod]["cantidad_total"] += cant
    resumen_ventas[prod]["ingresos_totales"] += cant * precio
for prod, datos in resumen_ventas.items():
    datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"]

print(resumen_ventas)
