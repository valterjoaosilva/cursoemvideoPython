from datetime import date
atual = date.today().year
for c in range(0, 7):
    dataNascimento = int(input("digite a data de nascimento: "))
    idade = atual - dataNascimento
    if(idade >= 21):
        print("{} anos".format(idade))
        print("maior idade")
    else:
        print("{} anos ".format(idade))
        print("Menor de idade")