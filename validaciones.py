def pedir_texto(mensaje):
    """
    Pide un texto al usuario y no permite que quede vacío.
    """
    texto = input(mensaje).strip()

    while texto == "":
        print("El campo no puede estar vacío.")
        texto = input(mensaje).strip()

    return texto


def pedir_entero_positivo(mensaje):
    """
    Pide un número entero positivo.
    Si el usuario se equivoca, vuelve a pedir el dato.
    """
    while True:
        dato = input(mensaje).strip()

        try:
            numero = int(dato)

            if numero > 0:
                return numero

            print("El número debe ser mayor que cero.")
        except ValueError:
            print("Debe ingresar un número entero válido.")


def pedir_rango(nombre_dato):
    """
    Pide un valor minimo y uno maximo.
    Si el usuario los ingresa al revés, los acomoda automáticamente.
    """
    minimo = pedir_entero_positivo(f"Ingrese {nombre_dato} mínima: ")
    maximo = pedir_entero_positivo(f"Ingrese {nombre_dato} máxima: ")

    if minimo > maximo:
        minimo, maximo = maximo, minimo

    return minimo, maximo
