class Retangulo:
    def __init__(self,largura,altura):
        self.largura=largura
        self.altura=altura
    def calcular(self):
        return self.largura*self.altura
        from RetanguloClass import  Retangulo

retangulo=Retangulo(10,20)
test=retangulo.calcular()
print(f"{test}")