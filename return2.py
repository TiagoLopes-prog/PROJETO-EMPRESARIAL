def inverte (nome,sobrenome):
    nomeinverso = sobrenome+" "+nome
    return nomeinverso
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
invertido = inverte(nome,sobrenome)
print("Olá", invertido)

