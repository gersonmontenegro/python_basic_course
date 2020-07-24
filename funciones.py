# def suma(a, b):
#     total = a + b
#     return total

# suma(0.1, 0.2)

def nombre_completo(nombre, apellido, inverso = False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'
# res = nombre_completo('Grs', 'Mnt', True)
res = nombre_completo(apellido = 'Mnt', nombre = 'GRS', inverso = True)
print(f'{res}')
