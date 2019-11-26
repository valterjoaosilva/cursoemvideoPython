nome = str(input("Informe seu nome completo: "))
print(nome.upper())
print(nome.lower())
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
separa = nome.split()
print(len(separa[0]))


