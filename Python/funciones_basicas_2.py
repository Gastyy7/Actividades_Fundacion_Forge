# 1) Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde el 0 hasta el número proporcionado como entrada.

# def multiplica_por_dos(num):
#     list = []
#     for i in range(num):
#         list.append(i)
#         list_multi = list[i] * 2
#         print(list_multi)

# multiplica_por_dos(3)

# 2) Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.

# def suma_y_resta(lista):
#     suma = 0
#     resta = 0 
#     for i in range(len(lista)):
#         suma += lista[i] 
#         resta -= lista[i]
#     print(f"Suma de la lista: {suma}")
#     print(f"Resta de la lista: {resta}")

# suma_y_resta([5, 2, 1, 4])

# 3) Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.

# def sumatoria_menos_longitud(list0):
#     sum = 0
#     resul = 0
#     for i in range(len(list0)):
#         sum += list0[i]
#     resul = sum - len(list0)
#     print(f"Resultado de suma de elementos de una lista menos longitud de la misma: {resul}")

# sumatoria_menos_longitud([10,10,10])

# 4) Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.

# def valores_multiplicados_segundo(numeros):
#     list1 = []
#     multi = 0
#     if len(numeros) >= 2:
#         for i in range(len(numeros)):
#             multi = numeros[i] * numeros[1]
#             list1.append(multi)
#         print(f'Longitud de lista: {len(list1)}, Elementos de la lista: {list1}')
#     else:
#         print(f'Lista vacia {list1}')

# valores_multiplicados_segundo([2, 1, 3])    

# 5) Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.

# def valor_multiplicado_longitud(valor, longitud):
#     nuevaLista = []
#     for i in range(longitud):
#         valor1 = valor * longitud
#         nuevaLista.append(valor1)
#     print(f'Nueva lista: {nuevaLista}')

# valor_multiplicado_longitud(3, 7)