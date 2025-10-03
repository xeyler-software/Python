import math

class Cubo:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return 6 * (self.lado ** 2)
    
    def volumen(self):
        return self.lado ** 3
