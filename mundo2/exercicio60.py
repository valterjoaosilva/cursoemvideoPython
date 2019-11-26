número = int(input("Digite um número: "))
c = 1
fatorial = 1
while c <= número:
    fatorial = fatorial * c
    c = c + 1

print("{}! = {}".format(número, fatorial))
