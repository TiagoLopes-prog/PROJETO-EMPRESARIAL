def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2
    return lista[n // 2]
