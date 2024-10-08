maca= int(input("Quantas maças você vai comprar?: "))
if maca >=12:
    valor = 0.25
    print("Valor da compra", maca*valor)
else:
    valor = 0.30
    print("Valor da compra: ", maca*valor)