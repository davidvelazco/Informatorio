# Clase Padre - Abstracta
class Vehiculo:

    def __init__(self, ruedas, modelo, motor, chasis):
        self.ruedas = ruedas
        self.modelo = modelo
        self.motor  = motor
        self.chasis = chasis

    def __str__(self):
        return f"Esto es un vehiculo de ruedas:{self.ruedas} Modelo: {self.modelo} Motor: {self.motor}"

    def sonido(self):
        pass

# Clase Hija
class Auto(Vehiculo):

    def __init__(self, ruedas, modelo, motor, chasis, puertas):
        super().__init__(ruedas, modelo, motor, chasis)
        self.puertas = puertas
    
    def sonido(self):
        return "PIPI 🚗"

# Clase Hija
class Moto(Vehiculo):

    def __init__(self, ruedas, modelo, motor, chasis, color):
        super().__init__(ruedas, modelo, motor, chasis)
        self.color = color
    
    def sonido(self):
        return "PII 🏍️"

auto_1 = Auto(4, "2024", "V8", "MASDJ-34", 5)

moto_1 = Moto(2, "2022", "103", "MDJ-4", "Azul")

print(auto_1.sonido())
print(moto_1.sonido())
