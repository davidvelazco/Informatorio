class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

class Empleado(Persona):
    def mostrar_nombre(self):
        return self._nombre

persona = Persona("Juan")
print(persona._nombre)
