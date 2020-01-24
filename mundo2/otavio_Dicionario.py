'''
DICIONARIO
'''
print('DICIONÁRIO')

dicionario = {1:"Valter", 2: 'Samira', 3: 'Pedro'}
print(dicionario)
print(dicionario[3])
print()
print('Criando Dicionário Modelo 2')

cabeça = dict( P1= 'valter', )

print('Incluindo Itens em um Dicionário')
dicionario[4] = 'Roberto'
print(dicionario)
print('-'*40)
print('Incluindo itens usando update')
dicionario.update({5:'Mariana'})
print(dicionario[5])
print('-'*40)
print('Apagando itens (DEL)')
del dicionario[2]
print(dicionario)
print(len(dicionario))
print('-'*30)
print('Diversar formas de acessar os valores de um dicionário')
print("Acessando a chave")
for k in dicionario:
    print(k)
print()
print('Acessando o valor da chave')
for k in dicionario.values():
    print(k)
print()
print('Acessando todos os itens do dicionário')
for k in dicionario.items():
    print(k)
print()
print('Chave e valor separados')
for k, v in dicionario.items():
    print(k, v)
print()




