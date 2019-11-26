c = 0
from random import randint
naleatorio = randint(0,10)
chute = int(input("informe seu chute: "))
while chute != naleatorio:
    c = c +1
    chute = int(input("Este não é o número sorteado, tente novamente, Informe sue chute>:"))

print("Você acertou o número é {} e você levou {} rodadas para acertar".format(naleatorio, c))