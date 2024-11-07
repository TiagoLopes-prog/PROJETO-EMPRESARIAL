def par():
    x = int(input("Valor: "))
    if (x)>=1:
        return "P"
    elif (x)<=-1:
        return "N"
    elif(x)==0:
        return "Zero"
print(par())