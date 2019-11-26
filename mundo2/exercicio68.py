from random import randint
print('-'*20)
print("vamos Jogar Par ou Impar")
print('-'*20)
contador = 0
while True:
    computador = randint(1,10)
    jogador = int(input("Digite seu valor: "))
    resultado = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Você quer Par ou Impar [P/I]: ")).strip().upper()[0]
    print(f"você jogou {jogador} o computador jogou {computador} o resultado foi {resultado}")
    if tipo == 'P':
        if resultado % 2 == 0:
            print("Você Venceu")
            contador = contador + 1
        else:
            print("Você Perdeu")
            break
    elif tipo == "I":
        if resultado % 2 == 1:
            print("Você Venceu")
            contador = contador + 1
        else:
            print("Você perdeu")
            break

