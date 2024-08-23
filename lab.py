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
        