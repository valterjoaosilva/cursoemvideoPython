numero = float(input("Digite o numero: "))
milhar = numero // 1000
restoMilhar = numero % 1000
centena = restoMilhar // 100
restoCentena = restoMilhar % 100
dezena = restoCentena // 10
restoDezena = restoCentena % 10
unidade = restoDezena // 1
print("unidade:{} ".format(unidade))
print("dezena: {} ".format(dezena))
print("centena: {}".format(centena))
print("milhar: {} ".format(milhar))


