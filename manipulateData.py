saltoDeLinea = '''Hola


Aqui hay varios salto de linea


'''

print(saltoDeLinea)


###################################

#llamar un caracter de un String
name = 'Brayan Torrealba S'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[-1])  # esta contara del final al principio



###################################



cadena = "Hola Mundo"
subcadena = cadena[0:4]  # "Hola" (del índice 0 al 3)
print(subcadena)

# También puedes usar índices negativos
subcadena_negativa = cadena[-5:]  # "Mundo" (los últimos 5 caracteres)
print(subcadena_negativa)



###################################


cadena = "Hola Mundo"

# Convertir a mayúsculas
mayusculas = cadena.upper()  # "HOLA MUNDO"
print(mayusculas)

# Convertir a minúsculas
minusculas = cadena.lower()  # "hola mundo"
print(minusculas)

# Reemplazar una subcadena
reemplazo = cadena.replace("Mundo", "Python")  # "Hola Python"
print(reemplazo)

# Dividir una cadena en una lista de subcadenas
lista_subcadenas = cadena.split(" ")  # ['Hola', 'Mundo']
print(lista_subcadenas)

# Unir una lista de cadenas en una sola cadena
unir = " ".join(lista_subcadenas)  # "Hola Mundo"
print(unir)

# Eliminar espacios en blanco al inicio y al final
cadena_espacios = "  Hola Mundo  "
cadena_limpia = cadena_espacios.strip()  # "Hola Mundo"
print(cadena_limpia)




###################################

cadena = "Hola Mundo"
posicion = cadena.find("Mundo")  # 5 (la posición donde empieza "Mundo")
print(posicion)

# Si la subcadena no se encuentra, find() retorna -1
no_encontrado = cadena.find("Python")  # -1
print(no_encontrado)
