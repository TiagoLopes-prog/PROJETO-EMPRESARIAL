class ControleRemoto:
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo
        self.ligado = False
        self.volume = 50

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.dispositivo} ligado.")
        else:
            print(f"{self.dispositivo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.dispositivo} desligado.")
        else:
            print(f"{self.dispositivo} já está desligado.")

    def ajustar_volume(self, valor):
        if 0 <= valor <= 100:
            self.volume = valor
            print(f"Volume do {self.dispositivo} ajustado para {self.volume}.")
        else:
            print("O volume deve estar entre 0 e 100.")

