# Aula de listas
# criando uma lista
lista = ['hamburguer', 'suco', 'laranja', 'gelatina']

# substituindo um item na lista por outro
lista[3] = 'sorvete'
print(lista)

# inserindo um novo item na lista adiciona ao final da lista
lista.append('chá')
print(lista)

# inserindo um novo item na lista em um local específico.
lista.insert(2, 'goiaba')
print(lista)

# apagar elementos da lista

# del especifique posição
del lista[3]

# pop é igual ao del, muda apenas que passa como parametro e a posição entre parentes
# no caso do pop se não passar o indice exemplo lista.pop() ele elimina o último elemento.
lista.pop(1)
print(lista)

# remove passa a posição especificando o objeto
lista.remove('sorvete')
print(lista)

# Criando uma lista com range:
valores = list(range(4, 12, 2))
print(valores)

# exemplos
# criando
relação = [4, 5, 2, 1, 8, 3, 10]

# colocando em ordem
relação.sort()
print(relação)

# colocando em ordem inversa
relação.sort(reverse=True)
print(relação)

# tamanho da lista
len(relação)
print(len(relação))

num = [2, 5, 9, 1]
print(num)
num [2] = 8
print(num)

num.append(12)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 15)
print(num)
num.pop(3)
len(num)
print(num)
print(len(num))

# criar um lista a partir do input
nomes = []
for nome in range(0, 5):
    nomes.append(str(input("Digite um nome: ")))
print(f"{nomes}")

#ligação entre listas
a = [2, 3, 4, 7]
b = a
# isso é uma ligação e não um cópia mudando o (a) o b também mudará
print(a)
print(b)

b[2] = 8

#o oito mudou nas duas listas
print(a)
print(b)

# copia de uma lista para outra
c = [4, 3, 7, 9]
d = c[:]
d[2] = 12
print(c)
print(d)

