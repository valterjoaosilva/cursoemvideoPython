'''
Funções - def em python
'''

def teste(resposta):
    print(resposta)

teste('Tudo foi conduzido')

def saudação(msg='Olá', nome='nome'):
    print(msg, nome)
saudação()
saudação(nome='Raquel')
saudação('oi', 'Vitor')
saudação(nome='Alencar', msg='Abraço')

def cumprimento(carro, bike):
    return f'{carro}, {bike}'

escolhas = cumprimento('alfa romeu', 'Cannodelo')
print(escolhas)

def divisão(n1, n2):
    return n1/n2

divide = divisão(8,4)
print(divide)

def dividindo(n1, n2):
    if n2 == 0:
        return
    return n1/n2

resultado = dividindo(122, 0)
if resultado:
    print(resultado)
else:
    print("não vale divisão por zero")

def cachorro():
    return ('doberman', 'piquines')#vira um tupla

tipo = cachorro()
print(tipo[0])

'''
desempacotando na lista 
'''
relação = [1, 2, 3, 4, 5]
print(*relação, sep='-')

def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1, 2, 3, 4, 5)



'''
castle em tupla para lista
'''
def reação(*args):
    args = list(args)
    args[0] = 20
    print(args)
reação(1, 3, 6, 78, 25)

def manuseio(*args):
    for v in args:
        print(v)
print('-'*40)
print('VARIANDO O EXEMPLO FAZENDO CALCULOS')
def manuseio(*args):
    for v in args:
        print(v*3)
manuseio(2, 4, 6, 6, 1)
print('-'*39)






riabe = manuseio(4, 67, 33, 56, 6 )



lista = [1, 2, 3, 4, 5,]
n1, n2, *n = lista
print(n1, n2, n)
print()
print('desempacotar')
desempacato = [2, 3, 6, 7, 8]
print(*desempacato, sep='-')
print('-'*40)
'''
funções def em python *args e **kwargs

'''
def func(a1, a2, a3, a4, a5, nome=None, sobrenome='Silva Junior'):
    print(a1, a2, a3, a4, a5, nome, sobrenome)
    return a1, a2, a3, a4, a5, nome, sobrenome

Aluno = func(1, 2, 3, 4, 5, nome='Valter João', sobrenome='Silva Junior')
print(Aluno[0], Aluno[5])

def exemplo(*args, **kwargs):
    print(args)
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

exemplo(20, 30, nome='Valter João', sobrenome='Silva Junior', idade= '51')

'''
Funçoes lambdas ou anonimas
'''
print('Exemplo 1')
a = lambda x, y: x*y
print(a(3,6))
print('-'*40)


print('-'*40)

print('FUNÇOES LAMBDAS')
print('SEM LAMBDA')
glosario = [[1, 'Roberto'],
            [2, 'Ronaldo'],
            [3, 'Roberval'],
            [4, 'Renato']
            ]
def tal(item):
    return (item[0])
glosario.sort(key=tal, reverse=True)
print(glosario)
print('-'*40)

print('COM LAMBDA')
glosario.sort(key=lambda item: item[0])
print(glosario)
print()
print('USANDO SORTED PARA ORDENAR')
print(sorted(glosario, key=lambda item: item[0]))






