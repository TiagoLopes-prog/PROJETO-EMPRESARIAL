def multiplica_pares(lista):
    resultado = 1
    for num in lista:
        if num % 2 == 0:
            resultado *= num
    return resultado
