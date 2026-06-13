from archivo_csv import guardar_paises
from config import ARCHIVO_CSV
from operaciones_paises import actualizar_pais, agregar_pais, buscar_pais
from operaciones_paises import filtrar_por_continente, filtrar_por_rango_poblacion
from operaciones_paises import filtrar_por_rango_superficie, mostrar_estadisticas
from operaciones_paises import ordenar_paises
from presentacion import mostrar_lista_paises


def mostrar_menu_principal():
    """
    Muestra las opciones principales del sistema.
    """
    print()
    print("Sistema de Gestión de Datos de Países")
    print("1. Mostrar todos los países")
    print("2. Agregar país")
    print("3. Actualizar población y superficie")
    print("4. Buscar país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("8. Guardar cambios")
    print("0. Guardar y salir")


def menu_filtros(paises):
    """
    Muestra el submenú de filtros.
    """
    while True:
        print()
        print("Filtros")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("0. Volver al menú principal")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            filtrar_por_continente(paises)
        elif opcion == "2":
            filtrar_por_rango_poblacion(paises)
        elif opcion == "3":
            filtrar_por_rango_superficie(paises)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def ejecutar_menu_principal(paises):
    """
    Ejecuta el ciclo principal del menú.
    Desde acá se llaman las funciones según la opción elegida.
    """
    while True:
        mostrar_menu_principal()
        opcion = input("Opción: ").strip()

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
            print("Opción inválida. Intente nuevamente.")
