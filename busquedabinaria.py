objetivo = int(input('Escribe un valor: '))
epsilon = 0.001
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
    print(f'Bajo: {bajo}, alto: {alto}')

print(f'La raiz cuadrada de {objetivo} es más o menos {respuesta}')
print(f'Iteraciones: {iteracion}')