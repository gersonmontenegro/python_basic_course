import pydash

# EAFP style
def busca_pais(paises, pais):
    """
    paises es un diccionario
    pais es la llave
    implementación principio EAFP
    """
    try:
        return paises[pais]
    except KeyError:
        return None

paises = ['Polombia', 'Chamozuela', 'Perú']
# print (paises.index('Persú'))
# result = pydash.collections.find(paises, lambda p: p == 'Pesrú')
# print(result)
# result = pydash.objects.find_key(paises, lambda p: p == 'Perú')
# print(result)

# LBYL style
def buscaPais(paises, pais):
    result = pydash.objects.find_key(paises, lambda p: p == pais)
    return result

print(f'LBYL style: {buscaPais(paises, "NombrePais")}')
