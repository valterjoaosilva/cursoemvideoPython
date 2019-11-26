número = int(input("Digite um número: "))
contador = 0
for c in range(2, número):
    if(número % c == 0):
        contador = contador + 1

if(contador >= 1):
    print("\33[34m Não é primo")
else:
    print("\33[35m É primo")


