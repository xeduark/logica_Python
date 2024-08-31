
biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}

def agregar_libro(biblioteca):
    titulo = input("Ingresa el título del libro: ").strip()
    autor = input("Ingresa el nombre del autor: ").strip()
    año = int(input("Ingresa el año de publicación: ").strip())
    
    biblioteca[titulo] = {"autor": autor, "año": año, "disponible": True}
    print(f'El libro "{titulo}" ha sido agregado a la biblioteca.')

def prestar_libro(biblioteca):
    titulo = input("Ingresa el título del libro para consultar si está disponible y prestarlo: ").strip()
    if titulo in biblioteca:
        if biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = False
            print(f"Acabas de prestar el libro '{titulo}'.")
        else:
            print(f"Disculpa, el libro '{titulo}' ya fue prestado.")
    else:
        print(f"El libro '{titulo}' no existe en la biblioteca.")

def devolver_libro(biblioteca):
    titulo = input("Ingresa el título del libro que deseas devolver: ").strip()
    if titulo in biblioteca:
        if not biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = True
            print(f'El libro "{titulo}" ha sido devuelto y ahora está disponible.')
        else:
            print(f'El libro "{titulo}" ya está disponible en la biblioteca.')
    else:
        print(f'El libro "{titulo}" no existe en la biblioteca.')

def mostrar_libros(biblioteca):
    print("\nLibros en la biblioteca:")
    for titulo, info in biblioteca.items():
        estado = "Disponible" if info["disponible"] else "No disponible"
        print(f'Título: {titulo}, Autor: {info["autor"]}, Año: {info["año"]}, Estado: {estado}')
    print()  # Línea en blanco para formato

def libros_por_ano(biblioteca, año):
    print(f"\nLibros publicados en el año {año}:")
    encontrado = False
    for titulo, info in biblioteca.items():
        if info["año"] == año:
            estado = "Disponible" if info["disponible"] else "No disponible"
            print(f'Título: {titulo}, Autor: {info["autor"]}, Estado: {estado}')
            encontrado = True
    if not encontrado:
        print(f'No se encontraron libros publicados en el año {año}.')
    print()  # Línea en blanco para formato
#MENU PARA LOS LIBROS
def menu():
    while True:
        print("\nMenú de la Biblioteca:")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Ver todos los libros")
        print("5. Ver libros por año")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            agregar_libro(biblioteca)
        elif opcion == "2":
            prestar_libro(biblioteca)
        elif opcion == "3":
            devolver_libro(biblioteca)
        elif opcion == "4":
            mostrar_libros(biblioteca)
        elif opcion == "5":
            año = int(input("Ingresa el año para buscar libros: ").strip())
            libros_por_ano(biblioteca, año)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 6.")

# Ejecución del menú
menu()
