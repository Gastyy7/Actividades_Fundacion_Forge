numero1 = 70 #Definiendo variable int
numero2 = 3.14 #variable float
booleano = False #Booleano
cadena = 'Hola Mundo' #string
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] #listas
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} #diccionario
frutas = ('guayaba', 'fresa', 'papaya') #tupla
print(type(frutas)) #impresion en consola   
print(ingredientes_pastel[2]) #impresion en cadena
ingredientes_pastel.append('Mantequilla')  #append para agregar un elemento a la lista
print(persona['nombre']) #impresion llamando un elemento de un diccionario
persona['nombre'] = 'Kevin' #cambiando el valor de un elemento de un diccionario
persona['color_ojos'] = 'cafe' #agregando un elemento con un valor en un diccionario
print(frutas[2]) #imprime en consola el elemento de la posicion 2 de la tupla frutas

if numero1 > 45: #condicional simple
    print("Numero mayor")
else:
    print("Numero menor")

if len(cadena) < 5: #añidamiento
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8): #buble for
    print(x)
for x in range(2,8):
    print(x)
for x in range(2,8,2):
    print(x)
x = 0
while(x < 8): #bucle while 
    print(x)
    x += 1

ingredientes_pastel.pop() #elimina y retorna el ultimo elemento de la lista
ingredientes_pastel.pop(1) #elimina y retorna el elemento del indice especificado

print(persona) #imprime diccionario
for clave in persona.keys(): #sacar solamente la clave sin el valor con keys
    if clave == 'pais':
        print(clave)
for valor in persona.values(): #sacar solamente el valor con values
    if valor == 35: 
        print(valor)
per = persona.pop('color_ojos') #elimina y retorna el valor del elemento color_ojos
print(per) #imprime la variable donde se guardo el pop de colo_ojos 
print(persona) #imprime diccionario

for ingrediente in ingredientes_pastel: #bucle for con añidamiento
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces(): #funcion con bucle for 
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces() #llamada de la funcion
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)