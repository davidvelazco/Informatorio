class Coche:
    ruedas = 4

    # Constructor
    def __init__(self, marca, color, puertas, motor, modelo):
        self.marca = marca
        self.color = color
        self.puertas = puertas
        self.motor = motor
        self.modelo = modelo

    # Para funcion print
    def __str__(self):
        return f"El auto es: {self.marca} {self.motor} {self.modelo} {self.color} {self.ruedas}"

    @classmethod
    def inc_ruedas(cls):
        cls.ruedas += 1

    @classmethod
    def dec_ruedas(cls):
        cls.ruedas -= 1

    @staticmethod
    def distancia(velocidad, tiempo):
        return velocidad * tiempo

