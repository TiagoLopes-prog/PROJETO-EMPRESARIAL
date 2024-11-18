def diferença_elementos_lista(lista):
    return [abs(lista[i] - lista[i+1]) for i in range(len(lista)-1)]
