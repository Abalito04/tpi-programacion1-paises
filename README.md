# TPI Programación 1 - Gestión de Datos de Países

Este proyecto es una aplicación de consola en Python que permite gestionar datos de países usando listas, diccionarios, funciones, condicionales, ciclos, lectura de archivos CSV, filtros, ordenamientos y estadísticas básicas.

## Archivos del proyecto

- `main.py`: archivo principal del programa. Contiene todas las funciones separadas por secciones internas: carga y guardado de CSV, validaciones, presentación, operaciones sobre países, filtros, ordenamientos, estadísticas y menú.
- `data/paises.csv`: dataset base con nombre, población, superficie y continente.

Nota: el archivo CSV está guardado en codificación UTF-8 con BOM para que los acentos y la ñ se vean correctamente al abrirlo en Excel o editores de Windows.

## Cómo ejecutar

1. Tener instalado Python 3.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

## Funcionalidades

- Cargar países desde un archivo CSV.
- Mostrar todos los países.
- Agregar un país nuevo.
- Actualizar población y superficie de un país.
- Buscar países por nombre, con coincidencia parcial o exacta.
- Filtrar por continente, rango de población o rango de superficie.
- Ordenar por nombre, población o superficie, de forma ascendente o descendente.
- Mostrar estadísticas:
  - País con mayor población.
  - País con menor población.
  - Promedio de población.
  - Promedio de superficie.
  - Cantidad de países por continente.
- Guardar cambios en el CSV.

## Ejemplo de uso

Entrada:

```text
Opcion: 4
Ingrese nombre o parte del nombre: arg
```

Salida:

```text
Listado de países
-------------------------------------------------------------------------------------
Argentina            | Población: 45376763     | Superficie: 2780400    km2 | Continente: América
-------------------------------------------------------------------------------------
```

## Integrantes

Integrante 1: Matias Emanuel Abalo

Integrante 2: Ignacio Nicolas Merlo

## Links

- Repositorio GitHub: https://github.com/Abalito04/tpi-programacion1-paises
- Video demostrativo: https://www.youtube.com/watch?v=LaGFrQpS2ag
- Documentación PDF: `Informe_TPI_Gestion_de_Datos_de_Paises.pdf`
