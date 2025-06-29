# Ejercicio: Tenemos que ingresar por pantalla un string con la fecha en formato ISO, por ejemplo
# '20250505', identificar el mes en el que se encuentra en este caso es mayo.

# Resolucion 1:
# fecha = input("Ingrese fecha en formato AAAAMMDD: ")
# meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", 
#          "septiembre", "octubre", "noviembre", "diciembre"]

# if len(fecha) == 8 and fecha.isdigit():
#     mes_ingresado = int(fecha[4:6])
#     if 1 <= mes_ingresado <= 12:
#         print(f"El mes es {meses[mes_ingresado - 1]}")
#     else:
#         print("La fecha ingresada no tiene el formato correspondiente...")
# else:
#     print("La fecha ingresada no tiene el formato correspondiente...")

# Resolucion 2:
fecha = input("Ingrese fecha en formato AAAAMMDD: ")
if fecha[4:6] == '01':
    print('El mes es enero')
elif fecha[4:6] == '02':
    print('El mes es feb')
elif fecha[4:6] == '03':
    print('El mes es mar')
elif fecha[4:6] == '04':
    print('El mes es abril')
elif fecha[4:6] == '05':
    print('El mes es mayo')
elif fecha[4:6] == '06':
    print('El mes es junio')
elif fecha[4:6] == '07':
    print('El mes es julio')
elif fecha[4:6] == '08':
    print('El mes es agosto')
elif fecha[4:6] == '09':
    print('El mes es septiembre')
