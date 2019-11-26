frase = str(input("Digite uma frase: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
for letra in range(len(junto) ):
    print(junto)
