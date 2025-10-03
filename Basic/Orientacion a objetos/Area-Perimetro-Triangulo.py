class trinagulo:
    def __init__(self, base, altura, lados):
        self.base = base
        self.altura = altura
        self.lados = lados
        
    def perimetro(self):
        return self.lados * 3
        
    def area(self):
        return (self.base * self.altura) / 2 

# Programa principal
def main():
    opcion = input("Ingrese la opción deseada (1: Perímetro y 2:Área ): ")
    if opcion not in ['1', '2']:
        print("Opción no válida.")
        
    elif opcion == '1':
        lados = float(input("Ingrese los lado del triángulo: "))
        t = trinagulo(lados, 0, lados)
        print("Perímetro del triángulo:", t.perimetro())
        
    else:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        t = trinagulo(base, altura,0)
        print("Área del triángulo:", t.area())

if __name__ == "__main__":
    main()