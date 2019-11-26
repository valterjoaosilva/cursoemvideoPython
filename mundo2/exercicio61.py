primeiro = int(input("Digite o termo inicial: "))
razão = int(input("Digite a razão: "))
décimo = primeiro + 10 * razão

while primeiro < décimo:
    print("{}".format(primeiro), end=', ')
    primeiro = primeiro + razão

print("fim")

#for c in range(primeiro, décimo, razão ):
