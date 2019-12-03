listaPalavra = "carro", "rodas", "bola", "pneu", "tabua", "media"
for palavra in listaPalavra:
    print(f"\n na palavra {palavra} temos a letras: => ", end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f"{letra}", end="  ")

print()