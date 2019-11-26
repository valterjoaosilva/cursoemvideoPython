primeiro = int(input("Digite o termo inicial: "))
razão = int(input("Digite a razão: "))
décimo = primeiro + 10 * razão
for c in range(primeiro, décimo, razão ):
    print("{}".format(c), end=', ')
print("fim")
