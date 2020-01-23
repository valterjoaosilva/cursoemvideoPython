'''
Listas comando para inserção e delete ect.
append, insert, pop, del, clear, extend, min, max.

'''

l1 = [1, 2, 3]
l2 = [4, 5, 6]
la = l1 +l2
l3 = [24, 45]
l4 = 36
l1.extend(l2) # extend inclui a em l1 o l2 como elemento e não com outra lista (apenas extende a lista)
l1.append(l3)
l2.insert(2, 48) # insere um objeto na posição indica

print(f"{l1}, {l2}, {l3}, {la}, {l4}")

l1.pop() #exclui o objeto definido, não especificando objeto exclui o último da lista
print(l1)

l1.insert(5, "caramelo")
print(l1)
del(l1[5])
print(l1)
l6 = list(range(0, 20))
print(l6)
print(max(l6))
print(min(l6))
l7 = []
l7.append(min(l6))
l7.append(max(l6))
print(l7)
print('='*40)
nomes = ['Valter', 'João', 'Silva', 'Junior']

for i in nomes:
    if i.startswith('J'):
        print(f'nomes começam com j:{i}')
    else:
        print(f'nomes que não começam com j: {i}')



