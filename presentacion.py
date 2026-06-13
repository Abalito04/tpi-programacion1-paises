def mostrar_pais(pais):
    """
    Muestra los datos de un país en una sola línea.
    """
    print(
        f"{pais['nombre']:<20} | "
        f"Población: {pais['poblacion']:<12} | "
        f"Superficie: {pais['superficie']:<10} km2 | "
        f"Continente: {pais['continente']}"
    )


def mostrar_lista_paises(paises):
    """
    Muestra una lista de países.
    Si la lista está vacía, informa que no hay resultados.
    """
    if len(paises) == 0:
        print("No hay países para mostrar.")
    else:
        print()
        print("Listado de países")
        print("-" * 85)

        for pais in paises:
            mostrar_pais(pais)

        print("-" * 85)
