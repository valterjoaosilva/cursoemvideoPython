class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.nomeclasse = self.__class__.__name__


class Cliente(Pessoa):
    def falar(self):
        print(f'{self.nomeclasse} de cpf {self.cpf } Sr(a): {self.nome} de {self.idade} anos Esta falando')


class ClienteVip(Cliente):
   def __init__(self, nome, sobrenome, idade, cpf):
       super().__init__(nome, idade, cpf)
       self.sobrenome = sobrenome

   def falar(self):
       print(f"{self.nomeclasse} de cpf {self.cpf} Sr(a): {self.nome} {self.sobrenome} de {self.idade} esta falando...")



