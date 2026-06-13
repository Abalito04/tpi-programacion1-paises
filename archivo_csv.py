import csv


def cargar_paises(nombre_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un país.
    """
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8-sig", newline="") as archivo:
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
                        print(f"Fila {numero_fila} ignorada: datos vacíos o valores no válidos.")
                    else:
                        pais = {
                            "nombre": nombre,
                            "poblacion": poblacion,
                            "superficie": superficie,
                            "continente": continente
                        }
                        paises.append(pais)
                except ValueError:
                    print(f"Fila {numero_fila} ignorada: población o superficie no son números enteros.")

    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}. Se iniciará con una lista vacía.")
    except OSError:
        print("Ocurrió un error al intentar leer el archivo CSV.")

    return paises


def guardar_paises(nombre_archivo, paises):
    """
    Guarda la lista de países en el archivo CSV.
    Esto permite conservar los cambios realizados desde el menú.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8-sig", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
        print("Datos guardados correctamente.")
    except OSError:
        print("No se pudieron guardar los datos en el archivo CSV.")
