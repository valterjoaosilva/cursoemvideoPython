#listas
print("Aula de Listas ")
print('-'*30)
print("Copiando listas")
dados = ['julio', 25, 'carla', 34, 'margo', 45,]
pessoas = list()
# append na estrutura.
pessoas.append(dados[:])
print(pessoas)
print(pessoas[0][0])
print(pessoas[0][1])
print(pessoas[0][4])

# Estrutura de listas dentro de listas
cadastro = [['Pedro', 28], ['Julia', 36], ['Amalia', 28]]
print(cadastro[2][0])
print(cadastro[2][0], cadastro[2][1])
print(f"{cadastro[2]}")

print()
# Estrutura chamando o indice principal
print("chamando o indice principal")
print(cadastro[1])

print()
print('--------------------')
print('Aula Prática')
aulaPratica = list()
aulaPratica.append('Valter')
aulaPratica.append(40)
print(aulaPratica)
testeAula = list()


print(testeAula)
aulaPratica[0] = 'Heitor'
aulaPratica[1] = 35
print(aulaPratica)
exemploAula = list()
exemploAula.append(aulaPratica[:])
print(exemploAula)
print(aulaPratica)

teste = list()
teste.append('valdori')
teste.append(44)
antiteste = list()
antiteste.append(teste[:])
teste[0] = 'carla'
teste[1] = 32
antiteste.append(teste[:])
print(antiteste)
print(teste)


