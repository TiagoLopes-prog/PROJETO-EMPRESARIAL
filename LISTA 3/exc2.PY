class Pessoa:
    def __init__(self,idade,nome):
            self.nome=nome
            self.idade=idade

            from PessoaClass import Pessoa

    test = Pessoa(16,"Tiago")
    print(f"{test.nome}\n{test.idade}")