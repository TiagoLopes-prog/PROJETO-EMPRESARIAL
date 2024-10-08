ano = int(input("digite o seu ano de nascimento: "))
if ano<2006:  
    print("Pode votar")
else:
    if ano>2006:
        print("Não pode votar")

    if ano==2006:
        print("pode votar")