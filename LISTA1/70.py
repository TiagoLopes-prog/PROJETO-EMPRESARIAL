def classifica_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    if a == b or b == c or a == c:
        return "Isósceles"
    return "Escaleno"
