lista = 'valter', 'julio', 'rogerio', 'carlos'
for nome in lista:
    if nome in 'rogerio':
        print(f"Achou {nome}")

for nome in lista:
    print(f"\nO nome é {nome}", end=' ')
    for letra in nome:
        if letra in 'crbaei':
            print(f'{letra}', end='  ')
print()
