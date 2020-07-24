frutas = ['manzana', 'pera', 'mango', 'papaya'] # lista
nombre = 'Mi nombre!' # cadena
tupla = ('a', 'b', 'c', 'd') # tupla
conjunto = {'a', 'b', 'c', 'd', 'e'} # conjunto
diccionario = {'a': 10, 'b': 20, 'c': 30}

# for fruta in frutas:
#     print(fruta)

# print(iter(1))

# iterator = iter(frutas)
# print(f'Iterator: {next(iterator)}')
# print(f'Iterator: {next(iterator)}')
# print(f'Iterator: {next(iterator)}')
# print(f'Iterator: {next(iterator)}')
# print(f'Iterator: {next(iterator)}')

# for item in diccionario.values():
#     print(item)

# for item in diccionario.keys():
#     print(item)

for item, item_value in diccionario.items():
    print(f'{item}:{item_value}')
