def potencia_recursiva(base, exp):
    if exp == 0:
        return 1
    return base * potencia_recursiva(base, exp - 1)
