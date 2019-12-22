print("lista livro python")
print("Média em lista")

print("Calculando Média")
'''
listmedia = [9, 6, 2, 5, 10]
soma = 0
cont = 0
media = 0
x = 0

while cont < 5:
    soma = soma + listmedia[cont]
    cont = cont + 1

media = soma / cont
print(f"{media}")

print("exemplo 2")

num = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    #num[x] = int(input("Num %d:"% (x+1)))
    num[x] = int(input(f"Digite o número {x + 1}: "))
    x = x + 1
while True:
    escolhido = int(input("que posição você quer imprimir(0 para sair): "))
    if escolhido == 0:
        break
    #print("Vocẽ escolheu o número: %d" % (num[escolhido - 1]))
    print(f"Você escolheu o número: {num[escolhido - 1]}")


print("acessando listas com nomes ")
nomes = ["a", "a", "a", "a", "a"]
x = 0
while x < 5:
    nomes[x] = str(input(f'Digite o nome na posição {x + 1} '))
    x = x + 1
while True:
    escolhido = int(input("Que posição Você quer imprimir? (0 para sair) : "))
    if escolhido == 0:
        break
    print(f"Você escolheu a posição {escolhido} o nome é: {nomes[escolhido - 1 ]}  ")

print("Iniciando a lista do Zero Usando Append")
nomes = []
x = 0

while x < 5:
    nomes.append(str(input(f"Digite o nome na posição {x + 1}: ")))
    x = x + 1
while True:
    escolhido = int(input(f"qual posição quer imprimir? (0 para sair) "))
    if escolhido == 0:
        break
    print(f"você escolheu a posição {escolhido} o nome na posição é: {nomes[escolhido - 1]}")
lista = [2, 6, 7, 4, 1]
print(f"{lista[0:-3]}")
print(f"{lista[-4]}")
print(f"{lista[0:5]}")

print("utilizando Len em Lista")
L = [2, 6, 7]
x = 0
while x < len(L):
    L[x] = L[x] * 2
    x = x +1

print(f"({L}")

print("Metodo append e extend")

lista1 = []
lista1 +=[2]
print(f"{lista1}")
lista1.append(3)
print(f"{lista1}")
lista1.extend([4])
print(f"{lista1}")
lista1.append([8, 12, 23])
print(f"{lista1}")
print(len(lista1))
del lista1[3]
print(lista1)
lista1 +=[34, 45, 67]
print(lista1)
#Criando uma lista a partir de um Range
print()
print("Criando uma lista a partir de um Range")
P = list(range(102))
print(P)
n = list(range(1, 34, 3))
print(n)
del P[34:97]
print(P)
'''


