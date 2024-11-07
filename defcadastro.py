def cadastro():
    name = input("Qual seu nome: ")
    age = int(input("Idade: "))

    return name, age

print("iniciando cadastro...")
nome,idade = cadastro()
print ("Cadastro realizado com sucesso: ")

print("Seu nome é ",nome,"E você tem",idade,"anos de idade")