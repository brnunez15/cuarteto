import json
from datetime import datetime
import os
from typing import List
from tabulate import tabulate

def cargar_alumnos(archivo_csv: str) -> List[dict]:
    """
    Función para cargar datos de los alumnos desde un archivo CSV sin usar csv.DictReader.
    Precondición: lee el archivo CSV con los datos del alumno (num de legajo, nombre y apellido, celular y mail)
    Postcondición: retorna una lista de diccionarios con los datos de los alumnos.
    """
    alumnos = []
    with open(archivo_csv, 'r', encoding="UTF-8") as f:
        lector_csv = csv.DictReader(f)
        for fila in lector_csv:
            alumnos.append(fila)
    return alumnos

def registrar_asistencias(alumnos: List) -> List[dict]:
    """
    Funcion para registrar asistencia de los alumnos
    precondicion: lee nombre, apellido y legajo del alumno y la fecha actual y pregunta si asistio o no
    postcondicion: imprime los datos del alumno y si asistio o no
    """
    asistencias = []
    fecha_actual = datetime.now().strftime("%d-%m-%Y")  # Obtener la fecha actual

    for alumno in alumnos:
        print(f"¿El alumno {alumno['nombre']} (LEGAJO: {alumno['legajo']}) asistió hoy ({fecha_actual})? (p/a)")
        asistencia = input("Ingrese el tipo de asistencia: ").strip().lower()

        
        while asistencia != 'p' and asistencia != 'a':
            print("Por favor ingrese 'p' o 'a'.")
            asistencia = input("Ingrese el tipo de asistencia: ").strip().lower()

        asistencias.append({
            "nombre": alumno['nombre'],
            "legajo": alumno['legajo'],
            "fecha": fecha_actual,
            "asistencia": asistencia
        })
    
    return asistencias


def guardar_asistencias_json(asistencias: List[dict], archivo_json: str) -> None:
    """
    Funcion para guardar las asistencias en el archivo json
    precondicion: recibe la informacion de asistencias
    postcondicion: guarda la informacion de las asistencias en un json
    """
    with open(archivo_json, 'w', encoding='UTF-8') as f:
        json.dump(asistencias, f, indent=4)


def main():
    """
    Funcion principal
    """
    archivo_alumnos = 'alumnos.csv'  
    archivo_asistencias = 'asistencias.json'  

    alumnos = cargar_alumnos(archivo_alumnos)
    asistencias = registrar_asistencias(alumnos)
    guardar_asistencias_json(asistencias, archivo_asistencias)

    print("Asistencias guardadas exitosamente en", archivo_asistencias)

def limpiar_consola() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu_alumno() -> None:
    """
    Funcion para mostrar el menu de los alumnos
    precondicion: recibe un numero del 1 al 4 para seleccionar el menu que se quiere ver
    postcondicion: devuelve la pantalla del menu seleccionado
    """
    menu_alumno = [
        ["1", "Ver mi porcentaje de asistencias"],
        ["2", "Ver mi total de asistencias"],
        ["3", "Ver mi total de inasistencias"],
        ["4", "Salir"]
    ]
    while True:  
        limpiar_consola()
        print(tabulate(menu, headers=["Opción", "Descripción"], tablefmt="rounded_grid"))
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Has seleccionado Ver mi porcentaje de asistencias.")
            
        elif opcion == "2":
            print("Has seleccionado Ver mi total de asistencias.")
            legajo_alumno = input("Ingrese su número de legajo: ")
            total_asistencias = asistencias("JSON/asistencias.json", legajo_alumno)
            print(f"Total de asistencias: {total_asistencias}")
            
        elif opcion == "3":
            print("Has seleccionado Ver mi total de inasistencias.")
            
        elif opcion == "5":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para continuar...")


def cargar_asistencias() -> None :
    
    ruta_actual = os.getcwd()
    carpeta_csv = os.path.join(ruta_actual, 'CSV')
    carpeta_json = os.path.join(ruta_actual, 'JSON')

    archivo_alumnos = os.path.join(carpeta_csv, 'alumnos.csv')
    archivo_asistencias = os.path.join(carpeta_json, 'asistencias.json')

    alumnos = cargar_alumnos(archivo_alumnos)
    asistencias = registrar_asistencias(alumnos)
    guardar_asistencias_json(asistencias, archivo_asistencias)


    print("Asistencias guardadas exitosamente")
    
    
def main() -> None:

    """
    Funcion principal
    """

    mostrar_menu_principal()

if __name__ == "__main__":
    main()