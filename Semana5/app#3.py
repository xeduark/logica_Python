#1. Crear un diccionario de alumnos y sus notas:
# Crea un programa que permita al usuario ingresar el nombre y la nota de un alumno, y almacene esta información en un diccionario.
# El programa debe permitir al usuario agregar varios alumnos y sus notas. Finalmente, el programa debe mostrar el diccionario con todos los alumnos y sus notas.
# Pista: Puedes utilizar un bucle "while" para que el programa siga pidiendo datos hasta que el usuario decida salir.
alumnos = {}
while True:
    nombre = input("Ingresa el nombre del alumno (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    while True:
        try:
            nota = float(input("Ingrese la nota del alumno:"))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Ingrese un valor númerico.")
    alumnos[nombre] = nota
print("\nListado de alumnos y sus notas:")
for alumno, nota in alumnos.items():
    print(f"{alumno}: {nota}")    
