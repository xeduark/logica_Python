
 

def eliminar_duplicados(lista_numeros):
    # Convertir la lista a un conjunto para eliminar duplicados
    conjunto_unicos = set(lista_numeros)
    
    # Convertir el conjunto de nuevo a una lista
    lista_sin_duplicados = list(conjunto_unicos)
    
    return lista_sin_duplicados

numeros = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
resultado = eliminar_duplicados(numeros)
print(resultado)

import random

def juego_adivinanza():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 7
    ha_adivinado = False

    print("¡Bienvenido al juego de adivinanza!")
    print("He escogido un número entre 1 y 100. Tienes 7 intentos para adivinarlo.")

    while intentos_restantes > 0 and not ha_adivinado:
        try:
            # Solicitar al usuario que ingrese un número
            intento = int(input("Introduce tu adivinanza: "))

            if intento < 1 or intento > 100:
                print("Por favor, introduce un número entre 1 y 100.")
                continue

            # Restar un intento
            intentos_restantes -= 1

            # Verificar si el usuario adivinó el número
            if intento == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} correctamente.")
                ha_adivinado = True
            elif intento < numero_secreto:
                print("El número secreto es mayor que tu intento.")
            else:
                print("El número secreto es menor que tu intento.")
            
            # Mostrar los intentos restantes
            if not ha_adivinado and intentos_restantes > 0:
                print(f"Te quedan {intentos_restantes} intentos.")
            elif intentos_restantes == 0:
                print(f"¡Se te han acabado los intentos! El número secreto era {numero_secreto}.")

        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido.")

# Iniciar el juego
juego_adivinanza()


def contar_vocales(frase):
    # Definir las vocales
    vocales = "aeiouAEIOU"
    contador_vocales = 0
    indice = 0

    # Usar un bucle while para recorrer la frase
    while indice < len(frase):
        # Verificar si el carácter actual es una vocal
        if frase[indice] in vocales:
            contador_vocales += 1
        # Incrementar el índice para seguir con el siguiente carácter
        indice += 1

    return contador_vocales

# Solicitar al usuario que ingrese una frase
frase_usuario = input("Ingresa una frase: ")

# Llamar a la función y mostrar el resultado
cantidad_vocales = contar_vocales(frase_usuario)
print(f"La frase contiene {cantidad_vocales} vocales.")


def calculadora():
    while True:
        print("\nCalculadora Básica")
        print("Selecciona una operación:")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")
        print("5. Salir")

        opcion = input("Elige una opción (1/2/3/4/5): ")

        if opcion == '5':
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break

        if opcion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Entrada no válida. Por favor ingresa números válidos.")
                continue

            if opcion == '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcion == '4':
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Opción no válida. Por favor elige una opción del 1 al 5.")

# Iniciar la calculadora
calculadora()


def crear_lista_pares():
    # Inicializar una lista vacía para almacenar los números pares
    lista_pares = []

    # Inicializar un contador en 1
    numero = 1

    # Usar un bucle while para recorrer los números del 1 al 100
    while numero <= 100:
        # Verificar si el número es par
        if numero % 2 == 0:
            # Agregar el número par a la lista
            lista_pares.append(numero)
        
        # Incrementar el contador en 1
        numero += 1

    return lista_pares

# Llamar a la función y mostrar la lista de números pares
numeros_pares = crear_lista_pares()
print("Números pares entre 1 y 100:", numeros_pares)



            
