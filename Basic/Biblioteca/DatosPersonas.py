datos1 = {
    "Nombre" : "Kevin",
    "Apellido" : "asd zxc",
    "Edad" : 19,
    "Ciudad" : "USA",
    "Lenguajes" : ["Python", "Java", "C++"]
}

datos2 = {
    "Nombre" : "zowl",
    "Apellido" : "nick",
    "Edad" : 20,
    "Ciudad" : "Lima",
    "Lenguajes" : ["Python", "Java", "C++"]
}

datos3 = {
    "Nombre" : "Leo",
    "Apellido" : "Gonzalez",
    "Edad" : 18,
    "Ciudad" : "Santiago",
    "Lenguajes" : ["Python", "Java", "C++"]
}

Estudiantes = [datos1, datos2, datos3]

print("Datos de los estudiantes:")

for i in range(len(Estudiantes)):
    print(f"Estudiante {i+1}:")

while(True):
    try:
        seleccion = int(input("Seleccione el número del estudiante: "))
        if 1 <= seleccion <= len(Estudiantes):
            estudiante = Estudiantes[seleccion - 1]
            print("\nDatos del estudiante seleccionado:")
            for clave, valor in estudiante.items():
                print(f"{clave}: {valor}")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Por favor, ingrese solo números.")