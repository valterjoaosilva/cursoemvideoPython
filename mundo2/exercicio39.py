anonascimento = int(input("Digite o ano de nascimento do jovem: "))
anoatual = 2019

idade = anoatual - anonascimento


if(idade < 18):
    print("Ainda vai se alistar")
elif(idade == 18):
    print("É hora de se alistar")
else:
    passou = idade - 18
    print("passou da hora de alistar")
    print("passou da idade de alistamento {} anos".format(passou))
