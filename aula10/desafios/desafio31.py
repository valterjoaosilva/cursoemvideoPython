distância = int(input("Informe a distância da viagem em Km: "))
if(distância <= 200):
    valor_viagem = distância * 0.50
    print("valor da viagem: {:.2f}".format(valor_viagem))
else:
    valor_viagem = distância * 0.45
    print("valor da viagem {:.2f}".format(valor_viagem))

