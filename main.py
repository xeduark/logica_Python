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