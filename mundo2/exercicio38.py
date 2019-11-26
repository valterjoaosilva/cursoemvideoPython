numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if(numero1 > numero2):
    print("{} é maior que {} ".format(numero1, numero2))
elif(numero2 > numero1):
    print("{} é maior que {}".format(numero2, numero1))
else:
    print("não existe valor maior")