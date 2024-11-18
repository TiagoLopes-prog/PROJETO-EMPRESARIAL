def soma_recursiva(n):
    return n + soma_recursiva(n - 1) if n > 0 else 0
