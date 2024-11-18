def soma_diagonais(matriz):
    return sum(matriz[i][i] for i in range(len(matriz))) + sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz)))
