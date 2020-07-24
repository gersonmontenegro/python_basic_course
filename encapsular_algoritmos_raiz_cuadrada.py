def buscarXaproximacion(objetivo, epsilon):
    iteracion = 0
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        iteracion += 1
    return respuesta

def buscarXenumeracion(objetivo):
    respuesta = 0
    iteracion = 0
    while respuesta**2 < objetivo:
        respuesta += 1
        iteracion += 1
    if respuesta**2 == objetivo:
        return respuesta
    else:
        return f'{objetivo} no tiene raíz cuadrada'

def buscarXbusquedaBinaria(objetivo, epsilon):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    iteracion = 0
    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
        iteracion += 1
    return respuesta

def crearOpciones(objetivo):
    algoritmo = int(input('Qué algoritmo deseas usar? [1] Búsqueda por enumeración. [2] Búsqueda por aproximación. [3] Búsqueda binaria '))
    if algoritmo == 1:
        res = buscarXenumeracion(objetivo)
    elif algoritmo == 2:
        res = buscarXaproximacion(objetivo, epsilon)
    else:
        res = buscarXbusquedaBinaria(objetivo, epsilon)
    return res

epsilon = 0.01
objetivo = int(input('Escribe un valor para encontrar la raiz: '))
res = crearOpciones(objetivo)
print(f'La raíz cuadrada de {objetivo} es: {res}')
