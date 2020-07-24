contador = 0
contador_interno = 0
contador_externo = 0
# while contador < 10:
#     print(contador)
#     contador = contador + 1

while contador_externo < 5:
    while contador_interno < 6:
        print(f'{contador_interno}-{contador_externo}')
        contador_interno = contador_interno + 1
        if contador_externo >= 3:
            break
    contador_externo = contador_externo + 1
    contador_interno = 0
