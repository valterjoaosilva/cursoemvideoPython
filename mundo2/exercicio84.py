principal = list()
turma = list()

qPessoas = 0
maior = menor = 0

while True:
    principal.append(str(input("Digite o nome da pessoa: ")))
    principal.append(int(input("digite o peso da pessoa: ")))
    if len(turma) == 0:
        maior = menor = principal[1]

    else:
        if maior < principal[1]:
            maior = principal[1]
        if menor > principal[1]:
            menor = principal[1]

    turma.append(principal[:])
    principal.clear()
    desejacontinuar = str(input("Você deseja continuar?[S/N]")).strip()
    if desejacontinuar in 'Nn':
        break
print(f"A turma são: {turma}")
print(f"A quantidade de Cadastros é: {len(turma)}")
print(f"o maior peso é: {maior} dos seguintes cadastros: ", end='')
for p in turma:
    if p[1] == maior:
        print(f'{p[0]}')
print()
print(f'O menor peso é: {menor} das seguintes cadastros: ', end='')
for p in turma:
    if p[1] == menor:
        print(f'{p[0]}')

