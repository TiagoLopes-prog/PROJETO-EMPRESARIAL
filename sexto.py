def soma_lista(lista):
    return sum(lista)


entrada = input("Digite os números separados por espaço: ")


numeros = [float(num) for num in entrada.split()]


print(f"A soma dos números é {soma_lista(numeros)}.")