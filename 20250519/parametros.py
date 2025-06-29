# def prueba_parametros(nombre, it_obj, dic_obj, mensaje="Hola"):
#     print(f"{mensaje} {nombre}")

#     for i in it_obj:
#         print(f"Imprimiendo cada elemento de *it_obj: {i}")

#     for k, v in dic_obj.items():
#         print(f"Imprimiendo cada elemento de *dic_obj: {k}:{v}")

# prueba_parametros("Lucas", [1,2,3,4,5], {1: 'uno', 2: 'dos', 3: "tres"})

# def prueba_parametros(nombre, mensaje="Hola", *it_obj, **dic_obj):
#     print(f"{mensaje} {nombre}")

#     for i in it_obj:
#         print(f"Imprimiendo cada elemento de *it_obj: {i}")

#     for k, v in dic_obj.items(): # {a:'uno', b:'dos', c:'tres'} --> ((a, uno), (b, dos), (c, tres))
#         print(f"Imprimiendo cada elemento de *dic_obj: {k}:{v}")

# prueba_parametros("Lucas", "Hola", 1, 2, 3, 4, 5, a='uno', b='dos', c='tres')



# dividendo = 10
# divisor = 2

# print(f"El modulo de {dividendo} y {divisor} es: {mod(dividendo, divisor)}")

# def f(x): # f(x)=x**2 + 3.x + 10
#     return x ** 2 + 3 * x + 10

# f(1)=0**2 + 3*0 + 10 =
#     = 0   +  0  + 10 = 10

# f(1)=1**2 + 3*1 + 10 =
#     = 1   +  3  + 10 = 14

# print(f(1))

def mod(dividendo, divisor):
    return dividendo % divisor

def calculo(numeros): # numeros = [1,2,3,4,5,6,7,8,9,10]
    pares = []
    impares = []
    for i in numeros:
        modulo = mod(i, 2)
        if modulo == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    print(f"El numero de pares es: {len(pares)}")
    print(f"El numero de impares es: {len(impares)}")

pares = [32,123,54456,76,234676,342,34]
impares = [32,123,23091,23907,1283,28937,34]

calculo([1,2,3,4,5,6,7,8,9,10,12,14])

print(f"Los numeros pares son {pares}")
print(f"Los numeros impares son {impares}")
