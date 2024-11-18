def aproxima_pi(n):
    pi = 0
    for i in range(n):
        pi += ((-1) ** i) / (2 * i + 1)
    return pi * 4
