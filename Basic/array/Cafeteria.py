cafes_disponibles = ["Cafe", "Cafe Americano", "Cafe Irlandes", "Cafe Britanico", "Cafe Latte"] 

print("Cafes disponibles: ")
for i in range(len(cafes_disponibles)):
    print(f"{i+1}. {cafes_disponibles[i]}")

while True:
    try:
        seleccion = int(input("Seleccione el numero del cafe que desea: "))
        if 1 <= seleccion <= len(cafes_disponibles):
            print(f"Usted ha seleccionado : {cafes_disponibles[seleccion - 1]}")
            break
        else:
            print("Opción no válida. Por favor, elija un número disponible.")
    except ValueError:
        print("Solo se permiten números, no letras ni símbolos.")