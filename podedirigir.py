idade = int(input("digite sua idade: "))
if idade == 16:  #Caso Verdadeiro
    print("Pode votar")
else:
    if idade>=16:
        print("Pode Dirigir")
    else:
        if idade <16:
            print("Apenas estude")