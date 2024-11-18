def substitui_texto_arquivo(nome_arquivo, palavra_antiga, palavra_nova):
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
    texto = texto.replace(palavra_antiga, palavra_nova)
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(texto)
