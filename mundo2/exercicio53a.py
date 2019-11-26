seuNome = str(input("Digite seu nome: ")).strip().upper()# retirando espaços em branco
nomeseparado = seuNome.split()#separado a frase no vetor por indice
nomePronto = ''.join(nomeseparado)#juntando toda a frase em uma única palavra.
detrasparafrente = "" #cria a variável para inverter a escrita da frase
for caracter in range(len(nomePronto) -1, -1, -1):
    detrasparafrente = detrasparafrente + nomePronto[caracter]
if(detrasparafrente == nomePronto):
    print("Deu certo")
else:
    print("Deu errado")
print("{} <____> {}".format(nomePronto, detrasparafrente))
