'''
getter e setter

'''

class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def desconto(self, percentual):
        self.preço = self.preço - (self.preço * (percentual / 100))




    #Getter
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, pessoa):
        self._nome = pessoa.title()

    @property
    def preço(self):
        return self._preço

    #Setter
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preço = valor




p1 = Produto('Camista', 45)
p1.desconto(10)
print(p1.nome, p1.preço)
print()
#um erro na base com inteiro configurado como string, saída getter e setter
p2 = Produto('CALÇA_JEANS', 'R$235.90')
p2.desconto(12.45)
print(f'{p2.nome}, {p2.preço:.2f}')
