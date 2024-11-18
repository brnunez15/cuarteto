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
    try:
        alumnos = []
    
        with open(archivo_csv, 'r', encoding="UTF-8") as f:
        
            lineas = f.readlines()
        
            encabezado = lineas[0].strip().split(",")
        
            for linea in lineas[1:]:
                valores = linea.strip().split(",")
                alumno = dict(zip(encabezado, valores))
                alumnos.append(alumno)
    
        return alumnos
    except FileNotFoundError:
        print(f"No se encontro el archivo {archivo_csv}")
    except UnicodeDecodeError:
        print("Error de codificacion en el archivo CSV")
    except ValueError:
        print("Error al convertir los datos del CSV")

def registrar_asistencias(alumnos: List) -> List[dict]:
    """
    Funcion para registrar asistencia de los alumnos
    precondicion: lee nombre, apellido y legajo del alumno y la fecha actual y pregunta si asistio o no
    postcondicion: imprime los datos del alumno y si asistio o no
    """
    try:
        asistencias = []
        fecha_actual = datetime.now().strftime("%d-%m-%Y") 

        for alumno in alumnos:
            while True:  
                print(f"¿El alumno {alumno['nombre']} (LEGAJO: {alumno['legajo']}) asistió hoy ({fecha_actual})? (p/a)")
                asistencia = input("Ingrese el tipo de asistencia: ").strip().lower()

                if asistencia == 'p' or asistencia == 'a':  
                    asistencias.append({
                        "nombre": alumno['nombre'],
                        "legajo": alumno['legajo'],
                        "fecha": fecha_actual,
                        "asistencia": asistencia
                    })
                    break
                else:
                    print("Por favor, ingrese 'p' para presente o 'a' para ausente.")

        return asistencias
    except KeyError as e:
        print(f"Error al acceder a un campo del alumno: {e}")
    except ValueError as e:
        print(f"Error al convertir el valor de asistencia: {e}")


def guardar_asistencias_json(asistencias: List[dict], archivo_json: str) -> None:
    """
    Funcion para guardar las asistencias en el archivo json
    precondicion: recibe la informacion de asistencias
    postcondicion: guarda la informacion de las asistencias en un json
    """
    try:
        with open(archivo_json, 'a', encoding='UTF-8') as f:
            json.dump(asistencias, f, indent=4)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error al guardar las asistencias: {e}")

def agregar_alumno_nuevo(archivo_csv: str):
    try:
        legajo = input("Ingrese el legajo del nuevo alumno: ")
        nombre = input("Ingrese el nombre del nuevo alumno: ")
        apellido = input("Ingrese el apellido del nuevo alumno: ")
        mail = input("Ingrese el correo electrónico del nuevo alumno: ")
        celular = input("Ingrese el número de celular del nuevo alumno: ")

        nueva_linea = f"{legajo},{nombre},{apellido},{mail},{celular}\n"

        with open(archivo_csv, 'a') as archivo:
            archivo.write(nueva_linea)
        print("Alumno agregado correctamente.")
    except IOError:
        print(f"No se pudo escribir el archivo {archivo_csv} Verifica los permisos de escritura")
        
def inasistencias(archivo_asistencias: str, legajo_alumno: str) -> int:
    """
    Función para contar el total de inasistencias de un alumno.
    Precondición: recibe el archivo JSON de asistencias y el número de legajo del alumno.
    Postcondición: devuelve el total de inasistencias del alumno.
    """
    try:
        total_inasistencias = 0

        with open(archivo_asistencias, 'r', encoding='UTF-8') as f:
            asistencias = json.load(f)

        for asistencia in asistencias:
            if asistencia["legajo"] == legajo_alumno and asistencia["asistencia"] == "a":
                total_inasistencias += 1

        return total_inasistencias
    except FileNotFoundError: 
        print(f"No se encontro el archivo {archivo_asistencias}")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {archivo_asistencias} Verifica el formato")
    except KeyError: 
        print(f"La clave 'legajo' o 'asistencia' no se encontro en el JSON")

def asistencias(archivo_asistencias: str, legajo_alumno: str) -> int:
    """
    Función para contar el total de asistencias de un alumno.
    Precondición: recibe el archivo JSON de asistencias y el número de legajo del alumno.
    Postcondición: devuelve el total de asistencias del alumno.
    """
    try:
        with open(archivo_asistencias, 'r', encoding='UTF-8') as f:
            asistencias = json.load(f)
            total_asistencias = sum(1 for asistencia in asistencias if asistencia["legajo"] == legajo_alumno and asistencia["asistencia"] == "p")

        return total_asistencias
    except FileNotFoundError: 
        print(f"No se encontro el archivo de asistencias {archivo_asistencias}")
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON de asistencias {e}")
    except KeyError:
        print("Error al buscar el legajo del alumno en el archivo JSON")

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
        print(tabulate(menu_alumno, headers=["Opción", "Descripción"], tablefmt="rounded_grid"))

        try:
            opcion = input("Seleccione una opción: ")
        except ValueError:
            print("Opcion invalida, por favor, ingrese un numero")
            continue

        if opcion == "1":
            print("Has seleccionado Ver mi porcentaje de asistencias.")
            
        elif opcion == "2":
            print("Has seleccionado Ver mi total de asistencias.")
            legajo_alumno = input("Ingrese su número de legajo: ")
            total_asistencias = asistencias("JSON/asistencias.json", legajo_alumno)
            print(f"Total de asistencias: {total_asistencias}")
            
        elif opcion == "3":
            print("Has seleccionado Ver mi total de inasistencias.")
            legajo_alumno = input("Ingrese su número de legajo: ")
            total_inasistencias = inasistencias("JSON/asistencias.json", legajo_alumno)
            print(f"Total de inasistencias: {total_inasistencias}")
            break
        elif opcion == "4":
            print("Saliendo...")
            break

        input("\nPresione Enter para continuar...")

def mostrar_menu_profesor() -> None:
    
    menu_profesor = [
        ["1", "Cargar asistencia o inasistencia"],
        ["2", "Cargar un nuevo alumno"],
        ["3", "Salir"]
    ]
    while True:  
        limpiar_consola()
        print(tabulate(menu_profesor, headers=["Opción", "Descripción"], tablefmt="rounded_grid"))
        
        try:
            opcion = input("Seleccione una opción: ")
        except ValueError:
            print("Opcion invalida, por favor, ingrese un numero")
            continue

        if opcion == "1":
            print("Has seleccionado Cargar Asistencia o Inasistencia.")
            cargar_asistencias()
       
        elif opcion == "2":
            print("Has seleccionado Cargar un nuevo alumno.")
            agregar_alumno_nuevo("CSV/alumnos.csv")
            
        elif opcion == "3":
            print("Saliendo...")
            break

        input("\nPresione Enter para continuar...")

def mostrar_menu_principal() -> None:
    menu_principal = [
        ["1", "Soy Alumno"],
        ["2", "Soy Profesor"],
        ["3", "Salir"]
    ]
    
    while True:  
        limpiar_consola()
        print(tabulate(menu_principal, headers=["Opción", "Descripción"], tablefmt="rounded_grid"))
        try:
            opcion = input("Seleccione una opción: ")
        except ValueError:
            print("Opcion invalida, por favor, ingrese un numero")

        if opcion == "1":
            print("Has seleccionado Alumno.")
            mostrar_menu_alumno()
       
        elif opcion == "2":
            print("Has seleccionado Profesor.")
            contrasenia = input("Ingrese la contraseña: ")
            if contrasenia == "1234":
                mostrar_menu_profesor()
            else: 
                print("Contraseña incorrecta.")

        elif opcion == "3":
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

if __name__ == "_main_":
    main()