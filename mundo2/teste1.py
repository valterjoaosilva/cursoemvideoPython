
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
# essa é uma tupla númerada, fazendo assim damos a ela o númeoo do contador
for pos, comida in enumerate(lanche):
    print(f'{comida} {pos}')


#imprime de forma organizada
print(sorted(lanche))

#junção de tuplas
a = 9, 5, 3, 2, 5, 12
b = 3, 24, 9, 2, 1, 4, 35
c = a + b
#colocando em ordem a junção,
print(sorted(c))
#lendo o tamanho da tupla
print(len(c))
#quantidade do referido elemento na tupla
print(c.count(9))
#qual posição do elemento na tupla
print(c.index(2))
