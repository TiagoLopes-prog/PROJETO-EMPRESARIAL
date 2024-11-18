def numeros_primos(n):
    return [x for x in range(2, n+1) if all(x % i != 0 for i in range(2, x))]
