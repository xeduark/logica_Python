#1. Sumar todos los elementos de una lista:

numeros = [1,2,3,4,5]
suma = 0
for numero in numeros:
    suma += numero

print(suma)    


#2. Contar la cantidad de elementos pares en una lista:

def contar_pares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    return len(pares)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad_pares = contar_pares(numeros)
print(cantidad_pares)


#3. Encontrar el elemento más grande de una lista:

def elemento_mas_grande(numeros):
    if len(numeros) == 0:  
        return None  

   
    mayor = numeros[0]
    
    
    for num in numeros[1:]:
        if num > mayor:  
            mayor = num
    
    return mayor


numeros = [3, 7, 1, 5, 9, 2]
mayor = elemento_mas_grande(numeros)
print(mayor)  

#4. Crear una nueva lista con los elementos de otra lista multiplicados por 2:












   


