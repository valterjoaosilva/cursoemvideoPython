numerica = [[], []]
for num in range(1, 8):
    valor = (int(input(f"Digite o {num}º um número: ")))
    if valor % 2 == 0:
        numerica[0].append(valor)
    else:
        numerica[1].append(valor)
print('-=' * 30)
print(numerica)
print('-=' * 30)
numerica[0].sort()
numerica[1].sort()
print(f'Os numeros pares são: {numerica[0]}', end=' ')
print(f'Os números impares são: {numerica[1]}', end=' ')
print()

