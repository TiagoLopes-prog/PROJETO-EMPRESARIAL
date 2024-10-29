salario = float(input("EScreva o seu salario atual: "))
if salario <= 280:
    porcentagem=salario*20/100
    salarionovo=salario+porcentagem
    print("Salario antigo",salario,"Salario novo", salarionovo,"aumento %20, valor do aumento de", porcentagem)
elif salario > 280 and salario<700:
    porcentagem=salario*15/100
    salarionovo=salario+porcentagem
    print("Salario antigo", salario,"")
