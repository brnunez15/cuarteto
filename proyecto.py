import csv
import json
from datetime import datetime
import os
from tabulate import tabulate

# Función para cargar los datos de los alumnos desde un archivo CSV
def cargar_alumnos(archivo_csv):
    alumnos = []
    with open(archivo_csv, 'r', encoding="UTF-8") as f:
        lector_csv = csv.DictReader(f)
        for fila in lector_csv:
            alumnos.append(fila)
    return alumnos

# Función para registrar la asistencia de los alumnos
def registrar_asistencias(alumnos):
    asistencias = []
    fecha_actual = datetime.now().strftime("%Y-%m-%d")  # Obtener la fecha actual

    for alumno in alumnos:
        print(f"¿El alumno {alumno['nombre']} (LEGAJO: {alumno['legajo']}) asistió hoy ({fecha_actual})? (si/no)")
        asistencia = input().strip().lower()
        
        # Validar entrada
        while asistencia not in ['si', 'no']:
            print("Por favor ingrese 'si' o 'no'.")
            asistencia = input().strip().lower()

        # Guardar la asistencia
        asistencias.append({
            "nombre": alumno['nombre'],
            "legajo": alumno['legajo'],
            "fecha": fecha_actual,
            "asistencia": asistencia
        })
    
    return asistencias

# Función para guardar las asistencias en un archivo JSON
def guardar_asistencias_json(asistencias, archivo_json):
    with open(archivo_json, 'w', encoding='UTF-8') as f:
        json.dump(asistencias, f, indent=4)

# Función principal para coordinar todo el flujo
def main():
    archivo_alumnos = 'alumnos.csv'  # Archivo CSV con datos de los alumnos
    archivo_asistencias = 'asistencias.json'  # Archivo JSON donde guardaremos las asistencias

    # Cargar los datos de los alumnos
    alumnos = cargar_alumnos(archivo_alumnos)

    # Registrar la asistencia
    asistencias = registrar_asistencias(alumnos)

    # Guardar las asistencias en el archivo JSON
    guardar_asistencias_json(asistencias, archivo_asistencias)

    print("Asistencias guardadas exitosamente en", archivo_asistencias)

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
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
            main()  # Llamar a la función main() para registrar asistencias
        elif opcion == "2":
            print("Has seleccionado Ver mi porcentaje de asistencias.")
            # Aquí puedes implementar la lógica para mostrar el porcentaje de asistencias
        elif opcion == "3":
            print("Has seleccionado Ver mi total de asistencias.")
            # Aquí puedes implementar la lógica para mostrar el total de asistencias
        elif opcion == "4":
            print("Has seleccionado Ver mi total de inasistencias.")
            # Aquí puedes implementar la lógica para mostrar el total de inasistencias
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para continuar...")

# Ejecutar el menú
if __name__ == "__main__":
    mostrar_menu()
