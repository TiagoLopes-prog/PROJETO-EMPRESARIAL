perg =  int(input("Telefonou para a vitima? 0-nao\n 1-sim\n "))


perg2 = int(input("Esteve no local do crime? 0-nao\n 1-sim\n "))


perg3 = int(input("Mora perto da vitima? 0-nao\n 1-sim\n "))


perg4 = int(input("Devia para a vitima? 0-nao\n 1-sim\n "))

perg5 = int(input("Ja trabalhou com a vitima? 0-nao\n 1-sim\n "))

valor = perg+perg2+perg3+perg4+perg5
print(valor)

if valor ==2:
    print("Suspeita")

elif valor == 3 or valor == 4:
    print("Cúmplice")

elif valor == 5:
        print("Assassino")

elif valor == 0 or valor ==1:
    print("Inocente")

