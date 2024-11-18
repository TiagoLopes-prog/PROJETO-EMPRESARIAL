from collections import Counter

def ocorrencias_palavras(texto):
    palavras = texto.split()
    return dict(Counter(palavras))
