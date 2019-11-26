anoNasc = int(input("Digite o ano de nascimento do Atleta: "))
anoAtual = 2019

idade = anoAtual - anoNasc

if (idade <= 9 ):
    print("Mirim")
elif(idade > 9 and idade <= 14):
    print("Infanto Juvenil ")
elif(idade >14 and idade <= 19):
    print("Juvenil")
elif(idade > 19 and idade <= 22):
    print("Cadete")
else:
    print("Adulto")

