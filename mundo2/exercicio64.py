n = int(input("Digite um número: "))
c = 0
i = 0
while n != 999:
    c = c + n
    i = i + 1
    n = int(input("Digite um número: "))
print('<=>'*10)
print("Foram digitados {} numeros".format(i))
print("A soma total {} ".format(c))
print('<=>'*10)