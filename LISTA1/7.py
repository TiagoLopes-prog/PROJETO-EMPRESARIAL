def conta_vogais(texto):
    return sum(1 for char in texto.lower() if char in 'aeiou')
