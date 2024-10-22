a=float(input("Escreva o numero: "))
b=float(input("Escreva o numero: "))

ca=float(input("Escreva o numero: "))
cb=float(input("Escreva o numero: "))

ano = 0 
while a<b:
    a+=a*ca
    b+=b*cb
    ano+=1
    print(ano)
