def calcular_raizes(a, b, c):

    delta = b**2 - 4 * a * c
    if delta < 0:

        print("A equação não possui raízes reais.")
    elif delta == 0:
    
        x1 = -b / (2 * a)
        print(f"A equação possui uma raiz real: x = {x1}")

    else:

        x1 = (-b + num.sqrt(delta)) / (2 * a)
        x2 = (-b - num.sqrt(delta)) / (2 * a)
        print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

calcular_raizes(a, b, c)
