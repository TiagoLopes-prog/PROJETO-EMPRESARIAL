class Bola:
    def __init__(self, cor, circunferencia, material):

        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):
    
        self.cor = nova_cor

    def mostra_cor(self):
        
        return self.cor

bola = Bola("azul", 30, "couro")
print("Cor inicial:", bola.mostra_cor()) 
bola.troca_cor("vermelho")
print("Nova cor:", bola.mostra_cor()) 