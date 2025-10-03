import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3, base=None, altura=None):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base if base else lado1
        self.altura = altura
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def area(self):
        # Si tiene base y altura, usa fórmula básica
        if self.base and self.altura:
            return (self.base * self.altura) / 2
        else:
            # Si no, usar fórmula de Herón
            s = self.perimetro() / 2
            return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

