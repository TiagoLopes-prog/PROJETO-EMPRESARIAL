def produto(a, b):
    if b == 0:
        return 0
    if b > 0:
        return a + produto(a, b - 1)
    return -produto(a, -b)
