valor1 = int(input("digite um numero: "))
valor2= int(input("digite outro numero: "))
valor3= int(input("digite outro numero: "))

if valor1 > valor2 > valor3:
    print("Em ordem crescente:", valor3, valor2, valor1)
elif valor3 > valor2 > valor1:
    print("Em ordem crescente", valor1, valor2, valor3)
elif valor2 > valor2 > valor1:
    print("Em ordem crescente", valor1, valor3, valor2)
elif valor1 > valor3 > valor2:
    print("Em ordem crescente", valor2, valor3, valor1)
elif valor3 > valor1 > valor2:
    print("Em ordem crescente:", valor2, valor1, valor3)
elif valor2 > valor1 > valor3:
    print("Em ordem crescente", valor3, valor1, valor2)
else:
    print("Valores iguais")
