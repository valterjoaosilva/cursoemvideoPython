listaNúmero = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze'

while True:
    número = int(input("Digite um número entre 0 e 14: "))
    if 0 <= número <= 14:
        break
    print('Tente novamente ', end='')
print(f"Você digitou o número {listaNúmero[número]}")

