# 03_consumoDatos.py

# Importar variables desde el archivo 02_tiposDeDatos.py
from tiposDeDatos import lista, tupla, conjunto, diccionario, nulo, byte_data, rango

# Obtener el primer elemento de la lista
primer_elemento_lista = lista[0]  # 1

# Obtener el segundo elemento de la tupla
segundo_elemento_tupla = tupla[1]  # 2

# Obtener un elemento del conjunto 
# (nota: los conjuntos no tienen un orden fijo)
# Para obtener un elemento, podemos convertir el conjunto en una lista primero
elemento_conjunto = list(conjunto)[0]  # 1 (Nota: el orden puede variar)

# Obtener el valor asociado a la clave 'nombre' y 'edad' en el diccionario
nombre_diccionario = diccionario['nombre']  # 'Brayan'
edad_diccionario = diccionario['edad']  # '28'

# Crear una variable que almacene un valor nulo (None)
valor_nulo = nulo  # None

# Obtener el primer byte de la secuencia de bytes
primer_byte = byte_data[0]  # 69 (correspondiente al carácter 'E')

# Obtener el primer número del rango
primer_numero_rango = rango.start  # 0

# Imprimir los resultados
print("Primer elemento de la lista:", primer_elemento_lista)
print("Segundo elemento de la tupla:", segundo_elemento_tupla)
print("Elemento del conjunto:", elemento_conjunto)
print("Nombre en el diccionario:", nombre_diccionario)
print("Valor nulo:", valor_nulo)
print("Primer byte de la secuencia de bytes:", primer_byte)
print("Primer número del rango:", primer_numero_rango)
