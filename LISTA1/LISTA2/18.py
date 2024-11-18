def media_ponderada(lista_valores, lista_pesos):
    return sum(v * p for v, p in zip(lista_valores, lista_pesos)) / sum(lista_pesos)
