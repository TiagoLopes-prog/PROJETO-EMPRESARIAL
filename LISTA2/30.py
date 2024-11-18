def histograma(lista):
    return {x: lista.count(x) for x in set(lista)}
