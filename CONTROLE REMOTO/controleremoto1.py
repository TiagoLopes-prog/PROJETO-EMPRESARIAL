class ControleSom(ControleRemoto):
    def __init__(self):
        super().__init__("Sistema de Som")
        self.bass = 50

    def ajustar_bass(self, valor):
        if 0 <= valor <= 100:
            self.bass = valor
            print(f"Bass ajustado para {self.bass}.")
        else:
            print("O valor de bass deve estar entre 0 e 100.")
