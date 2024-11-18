import math

def desvio_padrao(lista):
    media = sum(lista) / len(lista)
    return math.sqrt(sum((x - media) ** 2 for x in lista) / len(lista))
