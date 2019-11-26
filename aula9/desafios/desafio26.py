frase = str(input("Escreva a frase: ")).strip().upper()
contador = frase.count('A')
primeiroA = frase.find('A')
ultimoA = frase.rfind('A')
print("A letra A aparece na frase: {} vezes e a primeira letra aparece na posição: {} e a ultima na posição: {}"
      "".format(contador, primeiroA + 1, ultimoA + 1))

