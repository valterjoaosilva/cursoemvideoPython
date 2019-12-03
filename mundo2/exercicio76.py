produtos = 'notebook', 3250.00, 'impressora', 245.00, 'Smartphone', 1240.00, 'camera', 900.00, 'desktop', 1100.00
print('-'*40)
print(f'{"Lista de Produtos":^40}')
print('-'*40)
for n in range(0, len(produtos)):
    if n % 2 == 0:
        print(f"{produtos[n]:.<30}", end='')
    else:
        print(f"R${produtos[n]:>7.2f}")
print('-'*40)


