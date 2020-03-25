'''
atributos da classe devem ser alterados direto pela instância da classe, caso contrário ele não altera todas as instância.


'''


class A:
    vc = 123
    dc = 234

A1 = A()
A2 = A()

A1.vc = 132

print(A1.vc, A2.dc, A.vc)

