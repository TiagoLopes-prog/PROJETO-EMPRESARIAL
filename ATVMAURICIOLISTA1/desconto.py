produto = input ("informe o produto")
print(produto)
quant = int (input ("Quantidade do produto"))
print(quant)

valor = int(2)
print("o valor de cada produto é %s"%valor)

descontoi = int(input("percentual de desconto: "))
print(descontoi)

valorcomp = int(quant*valor)
descontof1 = int(valorcomp*descontoi) /100
valortotal = (valorcomp - descontof1)

print("total de compra: ", valortotal)