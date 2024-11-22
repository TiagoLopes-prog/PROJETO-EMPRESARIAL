class ControleTV:
    def __init__(self):
        super().__init__("TV")
        self.canal = 1

    def mudar_canal(self, canal):
        if canal > 0:
            self.canal = canal
            print(f"Canal da TV ajustado para {self.canal}.")
        else:
            print("Número de canal inválido.")