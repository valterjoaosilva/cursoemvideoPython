controle = []
pares = []
impares = []
while True:
    n = int(input("Digite um número: "))
    controle.append(n)
    opção = ' '
    while opção not in 'SsNn':
        opção = str(input("Deseja Continuar? [S/N]"))
    if opção in 'Nn':
        break
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista geral: {controle}, lista pares {pares}, lista impares {impares} ')

