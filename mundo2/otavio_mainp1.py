from random import randint

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(f'{self.ano_atual - self.idade}')

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(1, 99)
        return rand





p2 = Pessoa.por_ano_nascimento('Roger', 1972)
print(p2.nome, p2.idade)
p2.get_ano_nascimento()
print(p2.gera_id(), p2.nome, p2.idade)
