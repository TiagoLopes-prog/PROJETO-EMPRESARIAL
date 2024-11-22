class ControleRemote:
    def __init__(self,cor,altura,profundidade,largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def mudar_canal(self,botao):
        if botao=="+":
            print("Aumentar canal")

        elif botao=="-":
            print("dimunuir canal")
            
        else:
            print("valor inválido")