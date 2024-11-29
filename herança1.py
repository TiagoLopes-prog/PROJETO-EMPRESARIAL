class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def tipo_combustivel(self):
        return "Desconhecido"

    def capacidade_passageiros(self):
        return 0

class Carro(Veiculo):
    def tipo_combustivel(self):
        return "Gasolina"

    def capacidade_passageiros(self):
        return 5

class Moto(Veiculo):
    def tipo_combustivel(self):
        return "Gasolina"

    def capacidade_passageiros(self):
        return 2

class Caminhao(Veiculo):
    def tipo_combustivel(self):
        return "Diesel"

    def capacidade_passageiros(self):
        return 2

def mostrar_informacoes(veiculo):
    print(f"Marca: {veiculo.marca}")
    print(f"Modelo: {veiculo.modelo}")
    print(f"Tipo de Combustível: {veiculo.tipo_combustivel()}")
    print(f"Capacidade de Passageiros: {veiculo.capacidade_passageiros()}")
    print("-" * 20)

if __name__ == "__main__":
    carro1 = Carro("Toyota", "Corolla")
    moto1 = Moto("Honda", "CG 150")
    caminhao1 = Caminhao("Mercedes-Benz", "Actros")

    mostrar_informacoes(carro1)
    mostrar_informacoes(moto1)
    mostrar_informacoes(caminhao1)