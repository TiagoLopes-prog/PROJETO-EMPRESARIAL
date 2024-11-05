while True:
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    cal = int(input("Informe o calculo \n 1) adc \n 2)subt\n3)mult\n4)div"))

    calf = 0
    if cal ==1:
        calf = num1 + num2
        print('resultado',calf)
        if cal ==2:
            calf = num1 - num2
            print('Resultado',calf)

    try:
        if cal ==4:
                    calf = num1/num2
                    print('Resultado: ', calf)
                    
    except ZeroDivisionError:
                
                print("Não é possivel dividir por 0")

    continue 
