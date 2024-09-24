import os

nome = input("Nome = ")
idade = input("idade = ")
sexo = input("sexo = ")

nota1 = float(input("Primeita nota: "))
nota2 = float(input("Segunda nota: "))
os.system('cls')

print("Nome:",nome)
print("Idade:",idade)
print("Sexo:",sexo)


media = float(nota1 + nota2)/2
(print("Média:",media))