def eh_perfeito(n):
    return n == sum(i for i in range(1, n) if n % i == 0)
