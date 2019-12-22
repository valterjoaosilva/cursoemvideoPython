
lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
print(len(lanche))
#vai repetir a mensagem para cada lanche, comida é a variável contadora.
for comida in lanche:
    print(f"comi pra caramba {comida}")
#Imprime o tamanho do indice, neste caso do primeiro ao ultimo de 0 a 3.
for cont in range(0, len(lanche)):
    print(cont)
#neste caso o contado na hora da impressão é camado pela tupla então imprime cada item da memoria na posição.
for cont in range(0, len(lanche)):
    print(lanche[cont])
#imprime a tupla repetindo ela igual ao número de vezes do contador, nesse caso 4 vezes.
for cont in range(0, len(lanche)):
    print(lanche)
# essa é uma tupla númerada, fazendo assim damos a ela o número do contador
print()
print("tupla enumerada")
for pos, comida in enumerate(lanche):
    print(f'{comida} {pos:>20}', )
print()

#imprime de forma organizada
print("tupla organizada")
print(sorted(lanche))
print()
#junção de tuplas
a = 9, 5, 3, 2, 5, 12
b = 3, 24, 9, 2, 1, 4, 35
c = a + b
print()
#colocando em ordem a junção,
print("organizano a junção")
print(sorted(c))
#lendo o tamanho da tupla
print(len(c))
#quantidade do referido elemento na tupla
print(c.count(9))
#qual posição do elemento na tupla
print(c.index(2))
#diversos detalhes para manipular tuplas
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


