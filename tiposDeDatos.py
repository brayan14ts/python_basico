# Variables - Tipos de datos

# Entero (int)
number = 10  

# Flotante (float)
numberDecimal = 1.1  

# Cadena de texto (str)
string = 'Hola como estas'

# Booleano (bool)
boolean = True

# Lista (list) - Colección ordenada y mutable de elementos
lista = [1, 2, 3, 4, 5]  

# Tupla (tuple) - Colección ordenada e inmutable de elementos
tupla = (1, 2, 3, 4, 5)  

# Conjunto (set) - Colección desordenada de elementos únicos
conjunto = {1, 2, 3, 4, 5}  

# Diccionario (dict) - Colección de pares clave-valor
diccionario = {'nombre': 'Brayan', 'edad': 28}  

# Ningún valor (NoneType) - Representa la ausencia de valor
nulo = None  

# Byte (bytes) - Secuencia de bytes
byte_data = b'Esto es un byte'

# Rango (range) - Secuencia de números enteros
rango = range(10)  # De 0 a 9


##############################################
##############################################
##############################################
##############################################

# Crear un mensaje usando las variables
mensaje = f"{string}, me llamo {diccionario['nombre']} y tengo {diccionario['edad']} anios."
print(mensaje)

# Aquí estamos utilizando la f-string de Python (formato f"...") para insertar valores de las 
# variables dentro de una cadena de texto de forma sencilla y legible.


# El mismo mensaje usando el método format
mensaje = "{}, me llamo {} y tengo {} anios.".format(string, diccionario['nombre'], diccionario['edad'])
print(mensaje)

