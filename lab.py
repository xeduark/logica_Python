def prestar_libro(biblioteca):
    titulo = input("Ingresa el título del libro para consultar si esa disponible y prestarlo:").strip()
    if titulo in biblioteca:
        if biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = False
            print(f"Acabas de prestar el libro {titulo}.")
        else:
            print(f"Disculpa, el libro {titulo} ya fue prestado.")
    else:
        print(f"El libro {titulo} no existe.")

        print("Hola, soy Pablo")
print("Hola, soy Yonicua")
print("backyardigans")

def saludar(nombre):
    """
    Función que saluda a una persona.

    Args:
        nombre: El nombre de la persona a la que se saluda.

    Returns:
        Un mensaje de saludo.
    """
    return f"¡Hola, {nombre}!"

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    saludo = saludar(nombre)
    print(saludo)


def despedirse(nombre):
    """
    Función que se despide de una persona.

    Args:
        nombre: El nombre de la persona a la que se despide.

    Returns:
        Un mensaje de despedida.
    """
    return f"¡Adiós, {nombre}!"

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    saludo = saludar(nombre)
    print(saludo)
    despedida = despedirse(nombre)
    print(despedida)
#Jhonny

#nos tomamos un perico
print("faldecina")
        