from figuras.Rectangulo import Rectangulo
from figuras.Triangulo import Triangulo
from figuras.Cubo import Cubo

#Ejemplo si es en carpetas
#from Retos.Areas_Perimetos_Figuras.figuras.Rectangulo import Rectangulo

def pedir_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Error: Ingrese solo números válidos.")

def main():
    while True:
        print("\n=== Calculadora de Figuras ===")
        print("1. Rectángulo")
        print("2. Triángulo")
        print("3. Cubo")
        print("4. Salir")
        
        opcion = input("Seleccione una figura: ")

        if opcion == "1":
            base = pedir_numero_positivo("Ingrese la base: ")
            altura = pedir_numero_positivo("Ingrese la altura: ")
            rect = Rectangulo(base, altura)
            print("Área:", rect.area())
            print("Perímetro:", rect.perimetro())

        elif opcion == "2":
            print("Ingrese los lados del triángulo:")
            lado1 = pedir_numero_positivo("Lado 1: ")
            lado2 = pedir_numero_positivo("Lado 2: ")
            lado3 = pedir_numero_positivo("Lado 3: ")
            base = pedir_numero_positivo("Base: ")
            altura = pedir_numero_positivo("Altura: ")
            
            tri = Triangulo(lado1, lado2, lado3, base, altura)
            print("Perímetro:", tri.perimetro())
            print("Área:", tri.area())

        elif opcion == "3":
            lado = pedir_numero_positivo("Ingrese el lado del cubo: ")
            cubo = Cubo(lado)
            print("Área:", cubo.area())
            print("Volumen:", cubo.volumen())

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Error: Solo seleccione los números disponibles.")
            

# Ejecutar el programa
# Ejecutar
if __name__ == "__main__":
    main()
