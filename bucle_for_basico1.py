# for i in range(0,101): #Básico: imprime todos los números enteros del 0 al 100.
#     print(i)

# for i in range (2, 501, 2): #Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
#     print(i)

# for i in range(1, 101): #Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
#     if i % 10 == 0:
#         print("baby")
#     elif i % 5 == 0:
#         print("ice ice")
#     else:
#         print(i)

# suma = 0 #Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
# for x in range(0, 500001, 2):
#     suma += x
# print(suma)

# #Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
# for y in range(2024, 0, -3):
#     print(y)

# #Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
# numInicial = 3
# numFinal = 10
# multiplo = 2

# for t in range(numInicial, numFinal + 1):
#     if t % multiplo == 0:
#         print(t)
