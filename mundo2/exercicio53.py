frase = str(input("digite a frase: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
if (inverso == junto):
    print("Temos um palindro")
else:
    print("A frase não é um palindro")

print("{} -> {}".format(junto, inverso))