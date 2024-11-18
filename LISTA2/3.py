def conta_consoantes(texto):
    return sum(1 for c in texto.lower() if c in 'bcdfghjklmnpqrstvwxyz')
