def substitui_espaco():
    texto = input("Digite o texto: ")
    simbolo = input("Digite o símbolo para substituir os espaços: ")
    resultado = texto.replace(" ", simbolo)
    print(f"Texto com espaços substituídos: {resultado}")