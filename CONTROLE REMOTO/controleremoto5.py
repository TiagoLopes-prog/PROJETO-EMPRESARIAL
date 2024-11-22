class ControleVentilador(ControleRemoto):
    def __init__(self):
        super().__init__("Ventilador")
        self.velocidade = 1

    def ajustar_velocidade(self, velocidade):
        if 1 <= velocidade <= 3:
            self.velocidade = velocidade
            print(f"Velocidade do ventilador ajustada para {self.velocidade}.")
        else:
            print("Velocidade inválida. Escolha entre 1, 2 ou 3.")