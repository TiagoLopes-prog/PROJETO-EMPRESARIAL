def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    result = []
    while esquerda and direita:
        if esquerda[0] < direita[0]:
            result.append(esquerda.pop(0))
        else:
            result.append(direita.pop(0))
    return result + esquerda + direita
