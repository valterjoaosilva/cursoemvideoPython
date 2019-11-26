n = 0
c = 0
media = 0
soma = 0
maior = 0
menor = 0
while n == 0:
    while n != -1:
        n = float(input("digite um número: "))
        if n == -1:
            break
        soma = soma + n
        c = c + 1
        if c == 1:
            maior = menor = n

        if n > maior:
            maior = n
        if n < menor:
            menor = n

    media = soma/c
    print("A média é: {}".format(media))
    print("O menor número é: {} e o maior é: {}".format(menor, maior))
    print("você digitou {} números".format(c))
    opção = str(input("Você quer digitar mais números [S/N]? ")).upper().strip()[0]
    if opção in 'S':
        n = 0




