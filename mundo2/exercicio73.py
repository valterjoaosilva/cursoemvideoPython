tabelaBrasileirão = 'flamengo', 'palmeiras', 'santos', 'gremio', 'atletico paranaense', 'são paulo', 'internacional', 'corintians', 'goiais', 'bahia'

for posição in range(0, 5):
    print(f'{tabelaBrasileirão[posição]}', end=',')
print()
print(f'{tabelaBrasileirão[0:5]}')
for posição in range(6, 10):
    print(f'{tabelaBrasileirão[posição]}', end=',')
print()
print(f'{tabelaBrasileirão[-4:]}')
print(sorted(tabelaBrasileirão))


print(tabelaBrasileirão.index('são paulo')+1)