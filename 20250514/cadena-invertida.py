# Se ingresa por pantalla una cadena y se debe invertirla.
# No se puede usar [::-1] ni reverse
# Si la palabra que se ingreso es capicua/palindromos

cadena = input('Ingrese una palabra u oracion:')
invertida = ""
# hola
# h
# invertida = h(letra) + ''(invertida)
# o
# invertida = o(letra) + h(invertida)
# l
# invertida = l(letra) + oh(invertida)
# a
# invertida = a(letra) + loh(invertida)

for letra in cadena:
    invertida = letra + invertida

print(f"La cadena invertida se ve como: {invertida}")

if (invertida == cadena):
    print(f"La palabra {cadena} es capicua/palindromo")
else:
    print(f"La palabra {cadena} NO es capicua/palindromo")
