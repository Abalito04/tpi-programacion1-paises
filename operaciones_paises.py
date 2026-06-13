import unicodedata

from presentacion import mostrar_lista_paises
from validaciones import pedir_entero_positivo, pedir_rango, pedir_texto


def normalizar_texto(texto):
    """
    Convierte un texto a minúsculas y le quita los acentos.
    Sirve para que una búsqueda funcione aunque el usuario no escriba tildes.
    """
    texto = texto.lower()
    texto_normalizado = unicodedata.normalize("NFD", texto)
    texto_sin_acentos = ""

    for caracter in texto_normalizado:
        if unicodedata.category(caracter) != "Mn":
            texto_sin_acentos += caracter

    return texto_sin_acentos


def existe_pais(paises, nombre):
    """
    Verifica si ya existe un país con el mismo nombre.
    La comparación no distingue mayúsculas y minúsculas.
    """
    nombre_normalizado = normalizar_texto(nombre)

    for pais in paises:
        if normalizar_texto(pais["nombre"]) == nombre_normalizado:
            return True

    return False


def agregar_pais(paises):
    """
    Agrega un nuevo país a la lista.
    No permite campos vacíos ni números inválidos.
    """
    print()
    print("Agregar país")

    nombre = pedir_texto("Nombre: ")

    if existe_pais(paises, nombre):
        print("Ya existe un país con ese nombre.")
        return

    poblacion = pedir_entero_positivo("Población: ")
    superficie = pedir_entero_positivo("Superficie en km2: ")
    continente = pedir_texto("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    print("País agregado correctamente.")


def buscar_paises_por_nombre(paises, texto_busqueda):
    """
    Busca países por coincidencia parcial o exacta en el nombre.
    Por ejemplo, buscar 'arg' encuentra 'Argentina'.
    """
    encontrados = []
    texto_busqueda = normalizar_texto(texto_busqueda)

    for pais in paises:
        if texto_busqueda in normalizar_texto(pais["nombre"]):
            encontrados.append(pais)

    return encontrados


def buscar_pais(paises):
    """
    Pide un texto y muestra todos los países cuyo nombre coincida.
    """
    print()
    print("Buscar país por nombre")

    texto = pedir_texto("Ingrese nombre o parte del nombre: ")
    encontrados = buscar_paises_por_nombre(paises, texto)

    mostrar_lista_paises(encontrados)


def actualizar_pais(paises):
    """
    Actualiza población y superficie de un país.
    Se busca primero por nombre o parte del nombre.
    """
    print()
    print("Actualizar país")

    texto = pedir_texto("Ingrese nombre o parte del nombre del país: ")
    encontrados = buscar_paises_por_nombre(paises, texto)

    if len(encontrados) == 0:
        print("No se encontraron países con ese nombre.")
        return

    mostrar_lista_paises(encontrados)

    pais_a_actualizar = None

    if len(encontrados) > 1:
        nombre_exacto = pedir_texto("Hay varios resultados. Ingrese el nombre exacto a actualizar: ")

        for pais in encontrados:
            if normalizar_texto(pais["nombre"]) == normalizar_texto(nombre_exacto):
                pais_a_actualizar = pais
    else:
        pais_a_actualizar = encontrados[0]

    if pais_a_actualizar is None:
        print("No se encontró un país con ese nombre exacto.")
        return

    pais_a_actualizar["poblacion"] = pedir_entero_positivo("Nueva población: ")
    pais_a_actualizar["superficie"] = pedir_entero_positivo("Nueva superficie en km2: ")

    print("País actualizado correctamente.")


def filtrar_por_continente(paises):
    """
    Filtra los países por continente.
    """
    continente = normalizar_texto(pedir_texto("Ingrese continente: "))
    filtrados = []

    for pais in paises:
        if normalizar_texto(pais["continente"]) == continente:
            filtrados.append(pais)

    mostrar_lista_paises(filtrados)


def filtrar_por_rango_poblacion(paises):
    """
    Filtra los países cuya población esté dentro del rango indicado.
    """
    minimo, maximo = pedir_rango("poblacion")
    filtrados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            filtrados.append(pais)

    mostrar_lista_paises(filtrados)


def filtrar_por_rango_superficie(paises):
    """
    Filtra los países cuya superficie esté dentro del rango indicado.
    """
    minimo, maximo = pedir_rango("superficie")
    filtrados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            filtrados.append(pais)

    mostrar_lista_paises(filtrados)


def ordenar_por_nombre(pais):
    """
    Devuelve el nombre del país.
    Se usa como criterio para ordenar por nombre.
    """
    return pais["nombre"].lower()


def ordenar_por_poblacion(pais):
    """
    Devuelve la población del país.
    Se usa como criterio para ordenar por población.
    """
    return pais["poblacion"]


def ordenar_por_superficie(pais):
    """
    Devuelve la superficie del país.
    Se usa como criterio para ordenar por superficie.
    """
    return pais["superficie"]


def elegir_sentido_orden():
    """
    Permite elegir orden ascendente o descendente.
    Devuelve True si el orden debe ser descendente.
    """
    while True:
        print("1. Ascendente")
        print("2. Descendente")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            return False
        if opcion == "2":
            return True

        print("Opción inválida.")


def ordenar_paises(paises):
    """
    Ordena países por nombre, población o superficie.
    No modifica la lista original: crea una lista ordenada para mostrar.
    """
    print()
    print("Ordenar países")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        descendente = elegir_sentido_orden()
        ordenados = sorted(paises, key=ordenar_por_nombre, reverse=descendente)
        mostrar_lista_paises(ordenados)
    elif opcion == "2":
        descendente = elegir_sentido_orden()
        ordenados = sorted(paises, key=ordenar_por_poblacion, reverse=descendente)
        mostrar_lista_paises(ordenados)
    elif opcion == "3":
        descendente = elegir_sentido_orden()
        ordenados = sorted(paises, key=ordenar_por_superficie, reverse=descendente)
        mostrar_lista_paises(ordenados)
    else:
        print("Opción inválida.")


def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadísticas básicas del dataset.
    """
    if len(paises) == 0:
        print("No hay datos para calcular estadísticas.")
        return

    pais_mayor_poblacion = max(paises, key=ordenar_por_poblacion)
    pais_menor_poblacion = min(paises, key=ordenar_por_poblacion)

    suma_poblacion = 0
    suma_superficie = 0
    cantidad_por_continente = {}

    for pais in paises:
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1
        else:
            cantidad_por_continente[continente] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print()
    print("Estadísticas")
    print("-" * 60)
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km2")
    print()
    print("Cantidad de países por continente:")

    for continente, cantidad in cantidad_por_continente.items():
        print(f"- {continente}: {cantidad}")

    print("-" * 60)
