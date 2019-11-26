n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
n3 = int(input("Escreva o terceiro número: "))

if(n1>n2>n3):
    maior = n1
    menor = n3
elif(n1>n3>n2):
    maior = n1
    menor = n2
elif(n2>n1>n3):
    maior = n2
    menor = n3
elif(n2>n3>n1):
    maior = n2
    menor = n1
elif(n3>n1>n2):
    maior = n3
    menor = n2
elif(n3>n2>n1):
    maior = n3
    menor = n1
print("O maior é: {} e o menor é: {}".format(maior, menor))
