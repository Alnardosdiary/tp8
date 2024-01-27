
import json

archivo_alumnos = "alumnos.json"

def cargar_alumnos():
    try:
        with open(archivo_alumnos, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_alumnos(alumnos):
    with open(archivo_alumnos, "w") as file:
        json.dump(alumnos, file, indent=4)

def agregar_alumno():
    nombre = input("Nombre del alumno: ")
    apellido = input("Apellido del alumno: ")
    fecha_nacimiento = input("Fecha de nacimiento del alumno: ")
    dni = input("DNI del alumno: ")
    tutor = input("Nombre del tutor: ")
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": fecha_nacimiento,
        "dni": dni,
        "tutor": tutor,
        "notas": [],
        "faltas": 0,
        "amonestaciones": 0
    }
    alumnos.append(alumno)
    print("Alumno agregado con éxito.")

def mostrar_datos_alumno():
    dni = input("Ingrese el DNI del alumno: ")
    for alumno in alumnos:
        if alumno["dni"] == dni:
            print("Datos del alumno:")
            print(f"Nombre: {alumno['nombre']} {alumno['apellido']}")
            print(f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}")
            print(f"DNI: {alumno['dni']}")
            print(f"Tutor: {alumno['tutor']}")
            print(f"Notas: {', '.join(map(str, alumno['notas']))}")
            print(f"Cantidad de Faltas: {alumno['faltas']}")
            print(f"Cantidad de Amonestaciones: {alumno['amonestaciones']}")
            return
    print("No se encontró ningún alumno con ese DNI.")

def modificar_datos_alumno():
    dni = input("Ingrese el DNI del alumno: ")
    for alumno in alumnos:
        if alumno["dni"] == dni:
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_apellido = input("Nuevo apellido: ")
            nueva_fecha_nacimiento = input("Nueva fecha de nacimiento: ")
            nuevo_dni = input("Nuevo DNI: ")
            nuevo_tutor = input("Nuevo tutor: ")
            alumno["nombre"] = nuevo_nombre
            alumno["apellido"] = nuevo_apellido
            alumno["fecha_nacimiento"] = nueva_fecha_nacimiento
            alumno["dni"] = nuevo_dni
            alumno["tutor"] = nuevo_tutor
            print("Datos modificados con éxito.")
            return
    print("No se encontró ningún alumno con ese DNI.")

def expulsar_alumno():
    dni = input("Ingrese el DNI del alumno a expulsar: ")
    for i, alumno in enumerate(alumnos):
        if alumno["dni"] == dni:
            confirmacion = input(f"¿Estás seguro de expulsar al alumno {alumno['nombre']} {alumno['apellido']}? (S/N): ")
            if confirmacion.lower() == "s":
                del alumnos[i]
                print("Alumno expulsado con éxito.")
            else:
                print("La expulsión ha sido cancelada.")
            return
    print("No se encontró ningún alumno con ese DNI.")

alumnos = cargar_alumnos()

while True:
    print("=== Menú de Opciones ===")
    print("1. Agregar Alumno")
    print("2. Mostrar Datos de Alumno")
    print("3. Modificar Datos de Alumno")
    print("4. Expulsar Alumno")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        mostrar_datos_alumno()
    elif opcion == "3":
        modificar_datos_alumno()
    elif opcion == "4":
        expulsar_alumno()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
