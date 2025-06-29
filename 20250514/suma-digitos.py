# El usuario ingresa por pantalla una serie de numeros
# se debe sumas entre si la cadena ingresada, entra 99, 
# resultado 18. Ingresa 999, resultado 27
# Ingresa 101, el resultado es 2

#'99' --> numero = 99 -% 10-> suma = 9
numero = int(input('Ingrese un numero: '))
suma = 0

while numero > 0:
    print(numero % 10)
    suma = suma + (numero % 10)
    print(numero // 10)
    numero = numero // 10

print(f"La suma es de {suma}")
