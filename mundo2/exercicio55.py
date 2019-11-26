menor = 0
maior = 0
for p in range(1,6):
    peso = float(input("\33[m Digite peso da \33[34m {}ª pessoa:\33[m \33[36m ".format(p)))
    if(p == 1):
        maior = peso
        menor = peso
    else:
        if(peso > maior):
            maior = peso
        if(peso < menor):
            menor = peso
print("\33[m Menor => {}, Maior => {}".format(menor, maior))
