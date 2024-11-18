def produto_escalar(vetor1, vetor2):
    return sum(a * b for a, b in zip(vetor1, vetor2))
