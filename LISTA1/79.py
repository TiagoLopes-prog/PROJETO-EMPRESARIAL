def conta_palavras_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
    return len(texto.split())
