def conta_vogais(texto):
    return sum(1 for char in texto.lower() if char in 'aeiou')

# Solicita ao usuário para digitar o texto
texto = input("Digite um texto para contar as vogais: ")
print(f"O número de vogais no texto é: {conta_vogais(texto)}")