def conta_intervalo(lista, inicio, fim):
    return sum(1 for x in lista if inicio <= x <= fim)
