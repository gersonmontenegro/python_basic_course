def primera_letra(lista_de_palabras):
    primeras_letras = []
    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es un string (str)'
        assert len(palabra) > 0, f'No se permiten strings vacíos'
        primeras_letras.append(palabra[0])
    return primeras_letras

paises = ['Polombia', 114, 'Chamozuela', 'Perú']

print(f'--> {primera_letra(paises)}')