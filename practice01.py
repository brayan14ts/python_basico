# Ejercicio para practicar
# Intenta escribir un pequeño script que:
# 1 Pida al usuario que ingrese una frase.
# 2 Convierta toda la frase a mayúsculas.
# 3 Reemplace todas las apariciones de una palabra específica (que también se pide al usuario) por otra palabra.
# 4 Divida la frase en palabras y las imprima una por una.




# Pedir una frase al usuario
frase = input("Ingresa una frase: ")

# Convertir a mayúsculas
frase_mayusculas = frase.upper()

# Pedir la palabra a reemplazar y la nueva palabra
palabra_antigua = input("Ingresa la palabra que deseas reemplazar: ")
palabra_nueva = input("Ingresa la nueva palabra: ")

# Reemplazar la palabra
frase_reemplazada = frase_mayusculas.replace(palabra_antigua.upper(), palabra_nueva.upper())

# Dividir la frase en palabras
palabras = frase_reemplazada.split(" ")

# Imprimir las palabras
print("Las palabras de la frase son:")
for palabra in palabras:
    print(palabra)
