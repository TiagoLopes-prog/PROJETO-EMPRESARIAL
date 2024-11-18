def troca_vogais(s, nova_letra):
    return ''.join([nova_letra if char.lower() in 'aeiou' else char for char in s])
