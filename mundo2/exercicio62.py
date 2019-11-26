primeiro = int(input("Digite o termo inicial: "))
razão = int(input("Digite a razão: "))
décimo = primeiro + 10 * razão
contador = 10


while primeiro < décimo:
    print("{}".format(primeiro), end=', ')
    primeiro = primeiro + razão


opção = int(input("Quantos termos você quer mostrar mais?: "))
while opção != 0:
    contador = contador + opção
    enesimo = primeiro + opção * razão
    while primeiro < enesimo:
        print("{}".format(primeiro), end=', ')
        primeiro = primeiro + razão

    print("\n")
    opção = int(input("Quantos termos você quer mostrar mais?: "))

print("Progreção finalizada com {} termos".format(contador))

