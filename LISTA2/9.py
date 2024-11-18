def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    left = [x for x in lista[1:] if x < pivot]
    right = [x for x in lista[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
