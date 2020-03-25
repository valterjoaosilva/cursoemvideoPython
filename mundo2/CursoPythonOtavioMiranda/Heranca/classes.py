class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeclasse}: {self.nome} falando....")

class Cliente(Pessoas):
    def comprar(self):
        print(f'{self.nomeclasse}: {self.nome} Comprando...')



class Aluno(Pessoas):
    def estudar(self):
        print(f"{self.nomeclasse} {self.nome} Estudando...")