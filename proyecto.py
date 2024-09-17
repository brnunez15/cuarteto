import os
from tabulate import tabulate 

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

    print(tabulate(menu, headers=["Opción", "Descripción"], tablefmt="rounded_grid"))


def main():
    while True:
        limpiar_consola()  
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Has seleccionado Cargar asistencias o inasistencias.")
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
    main()

#COMENTARIOS