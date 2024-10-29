total = 0
while True:
    caixa = float(input("iforme um valor: "))
    if caixa >=1:
        total = total + caixa
        print("Produto: ", caixa)
    elif caixa==0:
        pag=float(input("Informe o valor do pagamento: "))
        print("\nTotal: ", total)
        print("Valor do pagamento", pag)
        print("Troco", pag - total)
    