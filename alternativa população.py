while True:
    caixa1 = float(input("informe um preço: "))
    caixa2 = float(input("informe um preço: "))
    caixa3 = float(input("informe um preço: "))
    caixa4 = float(input("informe um preço: "))

    total = caixa1 + caixa2 + caixa3 +caixa4 
    pag = float(input("Informe um valor: "))
    if pag<total:
        print("valor insuficiente")
        continue
    print("item1",caixa1)
    print("item1",caixa2)
    print("item1",caixa3)
    print("item1",caixa4)
    print("item1",total)
    print("Troco",pag - total)
    continue