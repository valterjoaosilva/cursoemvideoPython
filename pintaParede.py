largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))
area = largura * altura
qtinta = area / 2

print("A area total a ser pintada é: {:.2f} "
      "e a quantidade de tinta necessária é: {:.2f}.".format(area, qtinta))

