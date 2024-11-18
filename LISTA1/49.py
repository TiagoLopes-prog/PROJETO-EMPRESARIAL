def mdc_lista(lista):
    from functools import reduce
    return reduce(mcd, lista)
