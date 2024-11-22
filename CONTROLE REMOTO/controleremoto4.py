class ControleArCondicionado(ControleRemoto):
    def __init__(self):
        super().__init__("Ar-condicionado")
        self.temperatura = 24

    def ajustar_temperatura(self, temperatura):
        if 16 <= temperatura <= 30:
            self.temperatura = temperatura
            print(f"Temperatura ajustada para {self.temperatura}°C.")
        else:
            print("A temperatura deve estar entre 16°C e 30°C.")