nota = float(input("Escreva sua nota: "))
if nota >= 9.1 and nota <=  10:
    print("Nota: A, você foi aprovado")
elif nota >= 7.6 and nota <= 9.0:
    print("Nota: B, você foi aprovado")
elif nota >= 6.0 and nota <= 7.5:
    print("Nota C, você foi aprovado")
elif nota >= 4.1 and nota <= 5.9:
    print("Nota D, você foi reprovado")
elif nota <= 4.0:
    print("Nota E, você foi reprovado")