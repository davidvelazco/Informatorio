from coche import Coche

mi_auto_1 = Coche("Peugeot", "Rojo", 5, "M1.6", "2020")
mi_auto_2 = Coche("Peugeot", "Rojo", 3, "T200", "2025")
mi_auto_3 = Coche("Peugeot", "Rojo", 3, "T200", "2024")

# atributos
# mi_auto_1.color = "Azul"

# # atributos estaticos/clase
# print(mi_auto_1)
# print(mi_auto_2)
# print(mi_auto_3)

# mi_auto_1.dec_ruedas()

# print(mi_auto_1)
# print(mi_auto_2)
# print(mi_auto_3)

# mi_auto_3.inc_ruedas()

# print(mi_auto_1)
# print(mi_auto_2)
# print(mi_auto_3)

# staticmethod
dist = Coche.distancia(10, 3)
print(dist)
