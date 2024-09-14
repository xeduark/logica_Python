print("Ejercicio 1:")

# Escribe un programa que pida al usuario su nombre y apellido, y luego los imprima juntos en un mensaje de saludo.
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
#f-strings: Son más legibles y permiten insertar expresiones dentro de las llaves {}, lo que mejora la claridad del código.
print(f"Hola, tu nombre es {nombre} y tu apellido es {apellido}")

print("---------------------------------------------")
print("Ejercicio 2:")

#Crea una variable llamada precio con el valor 100. Calcula el precio con un descuento del 15% y muestra el precio final.
precio = 100
descuento = precio * 0.15
precio_con_descuento = precio - descuento
print(f"El precio con el descuento es: {precio_con_descuento}")

print("---------------------------------------------")
print("Ejercicio 3:")

#Escribe un programa que pida al usuario su edad y luego determine si es mayor o menor de edad.
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print(f"Eres mayor de edad porque tienes: {edad}")
else:
    print(f"Eres menor de edad porque tienes: {edad}")

print("---------------------------------------------")
print("Ejercicio 4:")

#Crea un programa que pida al usuario un número y determine si es par o impar.
numero_x = int(input("Ingresa un numero: "))
if numero_x % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

print("---------------------------------------------")
print("Ejercicio 5:")

#Escribe un programa que pida al usuario dos números y luego calcule su suma, resta, multiplicación y división.
numero_uno = int(input("Ingresa un numero: "))
numero_dos = int(input("Ingresa otro numero: "))
suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multi = numero_uno * numero_dos
divi = numero_uno / numero_dos if numero_dos != 0 else "No se puede dividir por cero"
print(f"la suma de los numeros es: {suma}")
print(f"la resta de los numeros es: {resta}")
print(f"la multiplicacion de los numeros es: {multi}")
print(f"la división de los numeros es: {divi}")

print("---------------------------------------------")
print("Ejercicio 6:")

#Crea un programa que pida al usuario su calificación y luego imprima el mensaje "Aprobado" si la calificación es mayor o igual a 70, o "Reprobado" si la calificación es menor que 70.
nota = int(input("Ingresa tu calificación para verificar si estás aprobado o reprobado: "))

if nota < 10 or nota > 100:
    print("La calificación ingresada es inválida. Debe estar entre 10 y 100.")
else:
    if nota >= 70:
        print(f"Tu calificación fue {nota} y estás APROBADO")
    else:
        print(f"Tu calificación fue {nota} y estás REPROBADO")

print("---------------------------------------------")
print("Ejercicio 7:")

#Escribe un programa que pida al usuario dos números y luego determine cuál es el mayor.
numero_a = int(input("Ingresa un numero: "))
numero_b = int(input("Ingresa otro numero: "))
if numero_a > numero_b:
    print(f"El numero {numero_a} es mayor que el numero {numero_b}")
elif numero_b > numero_a:
    print(f"El numero {numero_b} es mayor que el numero {numero_a}")
else:
    print(f"El numero {numero_a} y el numero {numero_b} son iguales")

print("---------------------------------------------")
print("Ejercicio 8:")

#Crea un programa que pida al usuario su nombre y luego imprima un mensaje de bienvenida con su nombre.
min_caracteres = 10
nombre_completo = input("Ingresa tu nombre completo, debe contener al menos 10 caracteres para un mensaje de bienvenida: ")

while len(nombre_completo) < min_caracteres:
    print(f"El texto debe contener al menos {min_caracteres} caracteres. Inténtalo de nuevo.")
    nombre_completo = input(f"Ingresa tu nombre completo con al menos {min_caracteres} caracteres para tu mensaje de bienvenida: ")

print(f"Bienvenido {nombre_completo} a nuestro sistema, es un gusto tenerte aquí.")

print("---------------------------------------------")
print("Ejercicio 9:")

#Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar de ese número hasta el 10.
numero_mul = int(input("Ingresa un numero para crear su tabla de multiplicar hasta el 10: "))
for x in range(1,11):
    resultado = numero_mul * x
    print(f"{numero_mul} x {x} = {resultado}")
    
print("---------------------------------------------")
print("Ejercicio 10:")

#Crea un programa que pida al usuario dos números y luego calcule su promedio.
print("Ingresa dos numeros para calcular su promedio")
numero_p1 = int(input("Ingresa el primer numero: ")
numero_p2 = int(input("Ingresa el segundo numero: "))
#Para calcular el promedio sumamos los numeros y luego lo dividimos entre la cantidad de numeros.
promedio = (numero_p1 + numero_p2) / 2
print(f"El promedio del numero {numero_p1} y el numero {numero_p2} es: {promedio}")