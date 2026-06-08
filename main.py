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