anio_actual = 2025
mayoria_edad = 18

anio_nac = int(input("Ingresar anio de nacimiento: "))

anio_usuario = anio_actual - anio_nac

if (anio_usuario >= mayoria_edad):
    print("El usuario es mayor de edad...")
else:
    print("El usuario NO es mayor de edad...")