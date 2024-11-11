def gerar_intervalo(num1, num2):
    
    inicio = min(num1, num2)
    fim = max(num1, num2)
    
    return list(range(inicio + 1, fim))

try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    
    intervalo = gerar_intervalo(numero1, numero2)
    print("Números no intervalo:", intervalo)
except ValueError:
    print("Por favor, insira apenas números inteiros.")

soma = 0

for i in range(numero1 = 1):
    soma += i
print(soma)



