'''
Split, join, enumerate em Python
Split Dividir uma string ou uma lista, separando cada palavra para um indice
join juntar uma lista
Enumarate Enumerar elementos de uma lista

'''
frase = "O Brasil acima de tudo Deus Acima de todos"
lista = frase.split(' ')
lista2 = frase.split(' , ')

print(lista)
print(lista2)

for valor in lista:
    print(f'A palavra {valor} aparece {lista.count(valor)}vezes na frase')

contagem = 0
palavra = 0
for valor in lista:
    qtd_Palavra = lista.count(valor)
    if qtd_Palavra > contagem:
        contagem = qtd_Palavra
        palavra = valor
print(f' A palavra que mais aparece é {palavra} e quantidade de vezes que aparece é {contagem}')

print('$'*40)

variante = 'Grande é o meu Deus, pequeno sou eu dependo de Deus'
oração = variante.split(' ')
print(oração)
entendo = '-'.join(oração)

print(entendo)
#print('-'.join(oração))

for l, p in enumerate(oração):
    #print(l, p)
    print(f'a palavra {p} esta na posição {l}')

'''
Desempacotamento

atribuir a uma variável o valor de uma lista, ação que enumerate faz automaticamente.
'''

banco = ["Julio", "Cesar", "Medina", "Clailton"]
n1, n2, n3, n4 = banco
print(n3)