
 

def eliminar_duplicados(lista_numeros):
    # Convertir la lista a un conjunto para eliminar duplicados
    conjunto_unicos = set(lista_numeros)
    
    # Convertir el conjunto de nuevo a una lista
    lista_sin_duplicados = list(conjunto_unicos)
    
    return lista_sin_duplicados

numeros = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
resultado = eliminar_duplicados(numeros)
print(resultado)


            
