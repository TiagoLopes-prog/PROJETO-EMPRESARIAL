class Quadrado:
    def __init__(self, tamanho_lado):

        self.tamanho_lado = tamanho_lado

    def mostrar_area(self):
        
        return self.tamanho_lado ** 2

    def mudar_valor_lado(self, novo_tamanho):
    
        self.tamanho_lado = novo_tamanho

    def mostrar_valor_lado(self):
    
        return self.tamanho_lado


quadrado = Quadrado(4)  
print(f"Tamanho do lado: {quadrado.mostrar_valor_lado()}")  
print(f"Área do quadrado: {quadrado.mostrar_area()}")  

quadrado.mudar_valor_lado(6)  
print(f"Novo tamanho do lado: {quadrado.mostrar_valor_lado()}")  
print(f"Nova área do quadrado: {quadrado.mostrar_area()}")  
