def conta_linhas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return sum(1 for _ in arquivo)
