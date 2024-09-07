# Ejercicios de Listas con For en Python
# 1. Sumar todos los elementos de una lista:

# Crea una función llamada suma_elementos que reciba una lista de números como parámetro y devuelva la suma de todos sus elementos.

# Pista: Puedes utilizar una variable para acumular la suma dentro del bucle "for".
def suma_elementos(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# 2. Contar la cantidad de elementos pares en una lista:

# Crea una función llamada contar_pares que reciba una lista de números como parámetro y devuelva la cantidad de elementos pares que contiene.

# Pista: Dentro del bucle "for", puedes verificar si cada elemento es divisible por 2.
def contar_pares(lista):
    cantidad_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            cantidad_pares += 1
    return cantidad_pares

# 3. Encontrar el elemento más grande de una lista:

# Crea una función llamada elemento_mas_grande que reciba una lista de números como parámetro y devuelva el elemento más grande de la lista.

# Pista: Puedes utilizar una variable para almacenar el elemento más grande encontrado hasta el momento.
def elemento_mas_grande(lista):
    if not lista:
        return None  # Devuelve None si la lista está vacía
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

# 4. Crear una nueva lista con los elementos de otra lista multiplicados por 2:

# Crea una función llamada multiplicar_elementos que reciba una lista de números como parámetro y devuelva una nueva lista con los elementos de la lista original multiplicados por 2.

# Pista: Puedes crear una nueva lista vacía y agregar los elementos multiplicados por 2 dentro del bucle "for".
def multiplicar_elementos(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(numero * 2)
    return nueva_lista

# 5. Invertir una lista:

# Crea una función llamada invertir_lista que reciba una lista como parámetro y devuelva una nueva lista con los elementos de la lista original invertidos.

# Pista: Puedes agregar los elementos de la lista original en orden inverso a la nueva lista.
def invertir_lista(lista):
    lista_invertida = []
    for numero in lista[::-1]:  # Usa el slicing para invertir la lista
        lista_invertida.append(numero)
    return lista_invertida
