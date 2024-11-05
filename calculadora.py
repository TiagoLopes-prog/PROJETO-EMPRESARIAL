while True:
    valor=int(input("Escolha: 1) Para adição\n2) Subtração\n3)Multiplicação\n4) Divisão\n 0) Para Sair: \n"))
    if valor == 0:
        print ("Saindo")
        break
    elif valor == 1:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        soma = num1 + num2
        print ("A soma dos dois numeros é: ", soma)
    elif valor == 2:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        sub = num1 - num2
        print ("a Subtração dos dois números é: ", sub)
    elif valor == 3:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        mult = num1 * num2
        print ("A multiplicação dos dois números é: ", mult)
    elif valor == 4:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        div = num1 / num2
        print ("A divisão dos dois números é: ", div)