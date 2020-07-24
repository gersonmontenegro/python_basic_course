import time

objetivo = int(input('Inserta un número: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0
tiempo_inicial = time.time()
iteracion = 0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    iteracion += 1
    # print(f'Respuesta: {respuesta}. Comparación: {abs(respuesta**2 - objetivo)}')

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es más o menos {respuesta}')

print(f'TIEMPO TOTAL: {time.time() - tiempo_inicial}')
print(f'TOTAL ITERACIONES: {iteracion}')
