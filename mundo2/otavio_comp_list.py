'''
compressão de listas em python
'''

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [l2v for l2v in l1]
print(l2)
print('='*40)
l3 = [v * 3.4 for v in l1]
print(l3)
print('='*40)
l4 = [(v, v1) for v in l1 for v1 in range(3)]
print(l4)
print('='*40)
ls = ['valter', 'carlos', 'rauli']
l5 = [v.replace('a', '@') for v in ls]
print(l5)

print('-'*40)

m3 = list(range(100))
m4 = [v for v in m3 if v % 2 == 0]
print(m4)

m5 = [v if v % 2 == 0 else 'pula' for v in m3]
print(m5)


