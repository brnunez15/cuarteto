import csv
import json
from datetime import datetime
import os
from tabulate import tabulate


def cargar_alumnos(archivo_csv):
    """
    Funcion para cargar datos de los alumnos desde un archivo CSV
    precondicion: lee el archico CSV con los datos del alumno(num de legajo, nombre y apellido, celular y mail)
    postcondicion: usa el archivo 
    """
    alumnos = []
    with open(archivo_csv, 'r', encoding="UTF-8") as f:
        lector_csv = csv.DictReader(f)
        for fila in lector_csv:
            alumnos.append(fila)
    return alumnos

def registrar_asistencias(alumnos):
    """
    Funcion para registrar asistencia de los alumnos
    precondicion: lee nombre, apellido y legajo del alumno y la fecha actual y pregunta si asistio o no
    postcondicion: imprime los datos del alumno y si asistio o no
    """
    asistencias = []
    fecha_actual = datetime.now().strftime("%Y-%m-%d")  # Obtener la fecha actual

    for alumno in alumnos:
        print(f"¿El alumno {alumno['nombre']} (LEGAJO: {alumno['legajo']}) asistió hoy ({fecha_actual})? (si/no)")
        asistencia = input().strip().lower()
        
        
        while asistencia not in ['si', 'no']:
            print("Por favor ingrese 'si' o 'no'.")
            asistencia = input().strip().lower()

        asistencias.append({
            "nombre": alumno['nombre'],
            "legajo": alumno['legajo'],
            "fecha": fecha_actual,
            "asistencia": asistencia
        })
    
    return asistencias


def guardar_asistencias_json(asistencias, archivo_json):
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

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    """
    Funcion para mostrar el menu
    precondicion: recibe un numero del 1 al 5 para seleccionar el menu que se quiere ver
    postcondicion: devuelve la pantalla del menu seleccionado
    """
    menu = [
        ["1", "Cargar asistencias o inasistencias"],
        ["2", "Ver mi porcentaje de asistencias"],
        ["3", "Ver mi total de asistencias"],
        ["4", "Ver mi total de inasistencias"],
        ["5", "Salir"]
    ]

    while True:
        limpiar_consola()
        print(tabulate(menu, headers=["Opción", "Descripción"], tablefmt="rounded_grid"))
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Has seleccionado Cargar asistencias o inasistencias.")
            contrasenia = int(input("Ingrese la contraseña: "))
            while contrasenia == 1234:
                print("Contraseña correcta, iniciando...")
                main()  
        elif opcion == "2":
            print("Has seleccionado Ver mi porcentaje de asistencias.")
            
        elif opcion == "3":
            print("Has seleccionado Ver mi total de asistencias.")
            
        elif opcion == "4":
            print("Has seleccionado Ver mi total de inasistencias.")
            
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    mostrar_menu()