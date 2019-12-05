números = []

while True:
    n = int(input("Digite um valor: "))
    if n not in números:
        números.append(n)
        print("Valor adicionado com sucesso.")
    else:
        print("Valor Duplicado, não será adicionado.")
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('-'*30)
print(sorted(números))
print('-'*30)