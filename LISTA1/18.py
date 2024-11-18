def alterna_maiusculas(texto):
    return ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(texto)])
