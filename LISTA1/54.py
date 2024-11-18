def media_notas(dicionario):
    return sum(dicionario.values()) / len(dicionario) if dicionario else 0
