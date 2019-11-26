from random import randint
naleatorio = randint(0,6)
chute = int(input("informe seu chute: "))
if chute == naleatorio:
    print("O número sorteado foi: {} e você acertou ".format(naleatorio))
else:
    print("jO número sorteado foi: {} e você errou".format(naleatorio))
