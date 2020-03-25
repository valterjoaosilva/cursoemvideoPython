'''
Associação (Agregação e composição
Uma clase usa outra classe e a classe precisa de outra classe
'''

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total = total + produto.valor
        print(total)



class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
