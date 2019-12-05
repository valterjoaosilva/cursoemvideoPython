num = []
maior = 0
menor = 0
for n in range(0, 5):
    num.append(int(input("Digite um número: ")))
    if n == 0:
        maior = menor = num[n]
    else:
        if num[n] > maior:
            maior = num[n]
        if num[n] < menor:
            menor = num[n]
print(f'Voce digitou os seguintes valores: {num}')
print(f"O maior número é {maior} nas posições ", end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(f" {i}", end=', ')
print(f"\nO menor número é {menor} posições são ", end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(f"{i}", end=', ')

print()
