from archivo_csv import cargar_paises
from config import ARCHIVO_CSV
from menus import ejecutar_menu_principal


def main():
    """
    Punto de entrada del programa.
    Carga los países desde el CSV y luego inicia el menú principal.
    """
    paises = cargar_paises(ARCHIVO_CSV)
    ejecutar_menu_principal(paises)


if __name__ == "__main__":
    main()
