from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("Suas Opções:"
      "[0] - Pedra"
      "[1] - Papel "
      "[2] - Tesoura ")

jogador = int(input("Digite sua opção: "))
print("Sua opção é: {}".format(itens[jogador]))
print("Computador escolheu: {}".format(itens[computador]))

