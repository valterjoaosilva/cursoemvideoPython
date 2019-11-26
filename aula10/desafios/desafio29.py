velocidade = int(input("Informe a velocidade: "))
if velocidade > 80:
    print("você foi multado")
    multa = (velocidade - 80) * 7
    print("valor da multa: {}".format(multa))
