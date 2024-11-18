def diagonais_matriz(matriz):
    return [matriz[i][i] for i in range(len(matriz))], [matriz[i][len(matriz)-1-i] for i in range(len(matriz))]
