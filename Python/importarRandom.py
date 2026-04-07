entero_decimal = float(12) #conversion de tipos
decimal_entero = int(24.3)
entero_complejo = complex(54)
print(entero_decimal, " ", decimal_entero, " ", entero_complejo)

import random #random
rand = random.randint(5,10)
print(rand)

print(f"Entero a decimal {entero_decimal}") #string.format()
print(f"Decimal a entero {decimal_entero}")
print(f"Entero a complex {entero_complejo}")

print("Entero a decimal %s" % (entero_decimal)) # %-formatting
print("Decimal a entero %s" % (decimal_entero))
print("Entero a complex %s" % (entero_complejo))

string = "Hola Mundo"

print(string.split("H"))

verso1 = ['dale', 'a', 'tu', 'cuerpo'] #Sumando y multiplicando listas
verso2 = ['alegria', 'macarena']
estrofa = verso1 + verso2
print(estrofa)
cancion = 3 * estrofa
print(cancion)

cajonera = ["pantalones", "camisetas", "calcetines"] #append
cajonera.append("vestidos") #Agregamos "vestidos" al final de la lista
print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines', 'vestidos']

lista_grande = [2, 4, 6, 8, 10, 12, 14, 16]

print(lista_grande[3:]) #Imprime:[8, 10, 12, 14, 16] #slicing
print(lista_grande[:7]) #Imprime:[2, 4, 6, 8, 10, 12]
print(lista_grande[3:6]) #Imprime:[8, 10, 12]

print(cajonera.index("pantalones")) #Devuelve el indice donde se encuentra el valor

num = 123
nombre = "Astrid"
print(f"Hola mundo {nombre} {num}") # cadena f
print("A %s le gustan los tacos de la tienda %a" % (nombre, num)) # .format()

personaje = {
    'nombre': 'Pepe',
    'apellido': 'Argento',
    'apodo': 'Papucho'
}

print(type(personaje))

for i in range(2, 8):
    print(f"Hola {num}")

estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:
   print(clave, estudiante[clave])

num1 = 5

while num1 < 4:
   print("bucle while -", num1)
   num1 += 1
else:
   print("Acabamos de salir del bucle")

x = 6

while x > 2:
   print(x)
   x -= 1
   if x == 3:
       break
else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break
   print("Sentencia final")