def apaga_vogais(s):
    return ''.join([char for char in s if char.lower() not in 'aeiou'])
