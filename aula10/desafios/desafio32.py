ano = int(input("informe o ano: "))
if(ano % 4 == 0):
    if(ano % 100 == 0):
        if(ano % 400 == 0):
            print("O ano é Bissexto ")
    elif(ano % 100 != 0):
        print("O ano é Bissexto ")
    else:
        print("O ano não é Bissexto ")
if(ano % 4 != 0):
    if(ano % 400 == 0):
        print("O Ano é Bissexto ")
    else:
        print("O Ano não é Bissexto ")