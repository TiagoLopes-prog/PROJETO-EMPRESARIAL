valor1 = int(input("digite um numero: "))
valor2= int(input("digite outro numero: "))

if valor1 < valor2:
    print("maior numero ", valor2)
    print("menor numero", valor1)
elif valor2 > valor1:
    print("maior numero",valor1)
    print("menor numero",valor2)
else:
    print("numeros iguais")
