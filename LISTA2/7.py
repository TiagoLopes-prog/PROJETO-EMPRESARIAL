def selection_sort(lista):
    for i in range(len(lista)):
        menor = min(lista[i:])
        lista.remove(menor)
        lista.insert(i, menor)
    return lista
