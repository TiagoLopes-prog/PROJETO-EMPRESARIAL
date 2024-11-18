def multiplica_matrizes(matriz1, matriz2):
    return [
        [matriz1[0][0] * matriz2[0][0] + matriz1[0][1] * matriz2[1][0],
         matriz1[0][0] * matriz2[0][1] + matriz1[0][1] * matriz2[1][1]],
        [matriz1[1][0] * matriz2[0][0] + matriz1[1][1] * matriz2[1][0],
         matriz1[1][0] * matriz2[0][1] + matriz1[1][1] * matriz2[1][1]]
    ]
