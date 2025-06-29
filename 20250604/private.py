class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def mostrar_nombre(self):
        return self.__nombre

persona = Persona("Juan")
# print(persona.__nombre)
# print(persona._Persona__nombre)
x = persona.mostrar_nombre()
print(x)
