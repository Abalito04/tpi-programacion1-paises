import csv


ARCHIVO_CSV = "paises.csv"


def cargar_paises(nombre_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un pais.
    """
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            # Verificamos que el CSV tenga las columnas esperadas.
            columnas_necesarias = {"nombre", "poblacion", "superficie", "continente"}
            if lector.fieldnames is None or not columnas_necesarias.issubset(lector.fieldnames):
                print("Error: el archivo CSV no tiene el formato correcto.")
                return paises

            for numero_fila, fila in enumerate(lector, start=2):
                try:
                    nombre = fila["nombre"].strip()
                    continente = fila["continente"].strip()
                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])

                    if nombre == "" or continente == "" or poblacion <= 0 or superficie <= 0:
                        print(f"Fila {numero_fila} ignorada: datos vacios o valores no validos.")
                    else:
                        pais = {
                            "nombre": nombre,
                            "poblacion": poblacion,
                            "superficie": superficie,
                            "continente": continente
                        }
                        paises.append(pais)
                except ValueError:
                    print(f"Fila {numero_fila} ignorada: poblacion o superficie no son numeros enteros.")

    except FileNotFoundError:
        print(f"No se encontro el archivo {nombre_archivo}. Se iniciara con una lista vacia.")
    except OSError:
        print("Ocurrio un error al intentar leer el archivo CSV.")

    return paises


def guardar_paises(nombre_archivo, paises):
    """
    Guarda la lista de paises en el archivo CSV.
    Esto permite conservar los cambios realizados desde el menu.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
        print("Datos guardados correctamente.")
    except OSError:
        print("No se pudieron guardar los datos en el archivo CSV.")


def pedir_texto(mensaje):
    """
    Pide un texto al usuario y no permite que quede vacio.
    """
    texto = input(mensaje).strip()
    while texto == "":
        print("El campo no puede estar vacio.")
        texto = input(mensaje).strip()
    return texto


def pedir_entero_positivo(mensaje):
    """
    Pide un numero entero positivo y repite la pregunta si el dato es invalido.
    """
    while True:
        dato = input(mensaje).strip()
        try:
            numero = int(dato)
            if numero > 0:
                return numero
            print("El numero debe ser mayor que cero.")
        except ValueError:
            print("Debe ingresar un numero entero valido.")


def pedir_rango(nombre_dato):
    """
    Pide un rango con minimo y maximo.
    Si el usuario ingresa el rango al reves, se intercambian los valores.
    """
    minimo = pedir_entero_positivo(f"Ingrese {nombre_dato} minima: ")
    maximo = pedir_entero_positivo(f"Ingrese {nombre_dato} maxima: ")

    if minimo > maximo:
        minimo, maximo = maximo, minimo

    return minimo, maximo

def mostrar_pais(pais):
    """
    Muestra los datos de un pais en una sola linea.
    """
    print(
        f"{pais['nombre']:<20} | "
        f"Poblacion: {pais['poblacion']:<12} | "
        f"Superficie: {pais['superficie']:<10} km2 | "
        f"Continente: {pais['continente']}"
    )


def mostrar_lista_paises(paises):
    """
    Muestra una lista de paises.
    Si la lista esta vacia, informa que no hay resultados.
    """
    if len(paises) == 0:
        print("No hay paises para mostrar.")
    else:
        print()
        print("Listado de paises")
        print("-" * 85)
        for pais in paises:
            mostrar_pais(pais)
        print("-" * 85)


def existe_pais(paises, nombre):
    """
    Verifica si ya existe un pais con el mismo nombre.
    La comparacion no distingue mayusculas y minusculas.
    """
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return True
    return False


def agregar_pais(paises):
    """
    Agrega un nuevo pais a la lista.
    No permite campos vacios ni numeros invalidos.
    """
    print()
    print("Agregar pais")
    nombre = pedir_texto("Nombre: ")

    if existe_pais(paises, nombre):
        print("Ya existe un pais con ese nombre.")
        return

    poblacion = pedir_entero_positivo("Poblacion: ")
    superficie = pedir_entero_positivo("Superficie en km2: ")
    continente = pedir_texto("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    print("Pais agregado correctamente.")


def buscar_paises_por_nombre(paises, texto_busqueda):
    """
    Busca paises por coincidencia parcial o exacta en el nombre.
    Por ejemplo, buscar 'arg' encuentra 'Argentina'.
    """
    encontrados = []
    texto_busqueda = texto_busqueda.lower()

    for pais in paises:
        if texto_busqueda in pais["nombre"].lower():
            encontrados.append(pais)

    return encontrados


def buscar_pais(paises):
    """
    Pide un texto y muestra todos los paises cuyo nombre coincida.
    """
    print()
    print("Buscar pais por nombre")
    texto = pedir_texto("Ingrese nombre o parte del nombre: ")
    encontrados = buscar_paises_por_nombre(paises, texto)
    mostrar_lista_paises(encontrados)


def actualizar_pais(paises):
    """
    Actualiza poblacion y superficie de un pais.
    Se busca primero por nombre o parte del nombre.
    """
    print()
    print("Actualizar pais")
    texto = pedir_texto("Ingrese nombre o parte del nombre del pais: ")
    encontrados = buscar_paises_por_nombre(paises, texto)

    if len(encontrados) == 0:
        print("No se encontraron paises con ese nombre.")
        return

    mostrar_lista_paises(encontrados)

    if len(encontrados) > 1:
        nombre_exacto = pedir_texto("Hay varios resultados. Ingrese el nombre exacto a actualizar: ")
        pais_a_actualizar = None

        for pais in encontrados:
            if pais["nombre"].lower() == nombre_exacto.lower():
                pais_a_actualizar = pais
    else:
        pais_a_actualizar = encontrados[0]

    if pais_a_actualizar is None:
        print("No se encontro un pais con ese nombre exacto.")
        return

    pais_a_actualizar["poblacion"] = pedir_entero_positivo("Nueva poblacion: ")
    pais_a_actualizar["superficie"] = pedir_entero_positivo("Nueva superficie en km2: ")
    print("Pais actualizado correctamente.")


def filtrar_por_continente(paises):
    """
    Filtra los paises por continente.
    """
    continente = pedir_texto("Ingrese continente: ").lower()
    filtrados = []

    for pais in paises:
        if pais["continente"].lower() == continente:
            filtrados.append(pais)

    mostrar_lista_paises(filtrados)


def filtrar_por_rango_poblacion(paises):
    """
    Filtra los paises cuya poblacion este dentro del rango indicado.
    """
    minimo, maximo = pedir_rango("poblacion")
    filtrados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            filtrados.append(pais)

    mostrar_lista_paises(filtrados)


def filtrar_por_rango_superficie(paises):
    """
    Filtra los paises cuya superficie este dentro del rango indicado.
    """
    minimo, maximo = pedir_rango("superficie")
    filtrados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            filtrados.append(pais)

    mostrar_lista_paises(filtrados)


def menu_filtros(paises):
    """
    Muestra el submenu de filtros.
    """
    while True:
        print()
        print("Filtros")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de poblacion")
        print("3. Filtrar por rango de superficie")
        print("0. Volver al menu principal")

        opcion = input("Opcion: ").strip()

        if opcion == "1":
            filtrar_por_continente(paises)
        elif opcion == "2":
            filtrar_por_rango_poblacion(paises)
        elif opcion == "3":
            filtrar_por_rango_superficie(paises)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")


def elegir_sentido_orden():
    """
    Permite elegir orden ascendente o descendente.
    Devuelve True si el orden debe ser descendente.
    """
    while True:
        print("1. Ascendente")
        print("2. Descendente")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            return False
        if opcion == "2":
            return True

        print("Opcion invalida.")


def ordenar_paises(paises):
    """
    Ordena paises por nombre, poblacion o superficie.
    No modifica la lista original: crea una lista ordenada para mostrar.
    """
    print()
    print("Ordenar paises")
    print("1. Nombre")
    print("2. Poblacion")
    print("3. Superficie")

    opcion = input("Opcion: ").strip()

    if opcion == "1":
        descendente = elegir_sentido_orden()
        ordenados = sorted(paises, key=lambda pais: pais["nombre"].lower(), reverse=descendente)
        mostrar_lista_paises(ordenados)
    elif opcion == "2":
        descendente = elegir_sentido_orden()
        ordenados = sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)
        mostrar_lista_paises(ordenados)
    elif opcion == "3":
        descendente = elegir_sentido_orden()
        ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=descendente)
        mostrar_lista_paises(ordenados)
    else:
        print("Opcion invalida.")


def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadisticas basicas del dataset.
    """
    if len(paises) == 0:
        print("No hay datos para calcular estadisticas.")
        return

    pais_mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])

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
    print("Estadisticas")
    print("-" * 60)
    print(f"Pais con mayor poblacion: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
    print(f"Pais con menor poblacion: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
    print(f"Promedio de poblacion: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km2")
    print()
    print("Cantidad de paises por continente:")

    for continente, cantidad in cantidad_por_continente.items():
        print(f"- {continente}: {cantidad}")

    print("-" * 60)


def mostrar_menu_principal():
    """
    Muestra las opciones principales del sistema.
    """
    print()
    print("Sistema de Gestion de Datos de Paises")
    print("1. Mostrar todos los paises")
    print("2. Agregar pais")
    print("3. Actualizar poblacion y superficie")
    print("4. Buscar pais por nombre")
    print("5. Filtrar paises")
    print("6. Ordenar paises")
    print("7. Mostrar estadisticas")
    print("8. Guardar cambios")
    print("0. Guardar y salir")


def main():
    """
    Funcion principal del programa.
    Carga los datos, muestra el menu y llama a las funciones segun la opcion elegida.
    """
    paises = cargar_paises(ARCHIVO_CSV)

    while True:
        mostrar_menu_principal()
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            mostrar_lista_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            menu_filtros(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "8":
            guardar_paises(ARCHIVO_CSV, paises)
        elif opcion == "0":
            guardar_paises(ARCHIVO_CSV, paises)
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
