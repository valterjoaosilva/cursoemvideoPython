'''
Métodos de orientado a objetos
public, protected, private
_ protected atributo público que não pode se acessado fora da classe
__ private atributo público que não pode ser acessado
'''

class BaseDeDados:
    def __init__(self): #Similar a um construtor da OO
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados ['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

print(bd._BaseDeDados__dados)
bd.inserir_cliente(1, 'Valter')
bd.inserir_cliente(4, 'Samira')
print(bd._BaseDeDados__dados)

bd.apaga_cliente(3)
bd.lista_clientes()


