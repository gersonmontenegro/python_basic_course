def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as err:
        print(f'Error: {err}')
        return lista
    except TypeError as err:
        print(f'Type error: {err}')
        return lista

# lista = list(range(10))
lista = [1, 2, 3, 4, 'a']
res = divide_elementos_de_lista(lista, 2)
print(res)