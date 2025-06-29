# lista_1 = ['String', 123, False]

# lista_2 = ['Cecilia', 'Lucas', 'Jonathan']

# lista_3 = ['Dato1', lista_1, 'Dato2', lista_2]

# print(lista_1)
# print(lista_2)
# print(lista_3)

# lista_1.append('Valor nuevo')

# print('Luego de agregar un valor')
# print(lista_1)
# print(lista_2)
# print(lista_3)

# lista = [0,1,2,3,4,5,6,7,8,9]
# lista_nueva = [i_1 if i_1 > 4 else False for i_1 in lista]
# print(lista_nueva)
# lista.reverse()
# lista_reversa = lista[::-1]
# print(lista_reversa)
# lista.append(10)
# print(lista)
# lista.remove(3)
# print(lista)

# tupla = (0,1,2,3,4,5,6,7,8,9,10,[100,200])
# print(tupla)
# lista = list(tupla)
# print(lista)
# lista.append(13)
# print(lista)

# tupla = tuple(lista)
# print(tupla)

# Crear una lista nueva, con los elementos potenciados por si mismos
# 0 ** 0, 4 ** 4...
# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# numeros_potenciados = [pow(x, x) for x in numbers]
# print(numeros_potenciados)
lenguajes_p = ['java', 'python', 'go', 'rust']
len_corregidos = [leng[0].upper() + leng[1::] for leng in lenguajes_p]
print(len_corregidos)
