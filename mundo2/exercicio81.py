numeros = []
contNum = 0

while True:
    n = int(input("Digite um número:"))
    numeros.append(n)
    contNum = contNum + 1
    desejaContinuar = ' '
    while desejaContinuar not in 'SsNn':
        desejaContinuar = str(input("Deseja Continuar? [S/N]"))

    if desejaContinuar in 'Nn':
        break
print(f"Foram digitados {contNum} números")
numeros.sort(reverse=True)
print(f"{numeros}")

if 5 in numeros:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")


