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
print("listas dentro de listas")
print("="*30)
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
print()
print("Aula Prática 2 usando for")
print('-'*40)
cadastramento = [['heitor vila lobos', 'músico'], ['joseph bach', 'compositor'],
                 ['monet', 'pintor'], ['vangohf', 'artista plastico']]
for p in cadastramento:
    print(p)
    print(p[0])
    print(p[1])
    print()
for p in cadastramento:
    print(f'{p[0]} é {p[1]}.  ')
print()

# Inserindo dados em uma lista com for
print("inserindo dados em uma lista com for")
print('-'*40)
pasta = list()
negócio = list()
totalmaior = totalmenor = 0

for i in range(0, 3):
    pasta.append(str(input("Digite o nome: ")))
    pasta.append(int(input("Digite a idade")))

print(pasta)
for p in pasta:
    print(p)

for p in pasta:
    print(f'{p} anos de idade')

for p in pasta:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1

print(f'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade')

print()









