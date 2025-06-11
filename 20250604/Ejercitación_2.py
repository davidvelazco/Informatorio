class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera):
        super().__init__(nombre, apellido)
        self.carrera = carrera

    def mostrar_carrera(self):
        return f"{self.nombre_completo()} estudia {self.carrera}"

estudiante = Estudiante("David", "Velazco", "programación en Python")
print(estudiante.mostrar_carrera())