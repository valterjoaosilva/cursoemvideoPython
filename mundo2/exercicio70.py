somaPreço = preçoMais1000 = produtoBarato = c = preçoMaisBarato =  0
print("#"*30)
print("EMPÓRIO ARMANY ")
print("#"*30)
while True:
    nomeProduto = str(input("Digite o Nome do Produto: ")).strip()
    preço = int(input("digite o preço: "))
    somaPreço = somaPreço + preço
    if preço > 1000:
        preçoMais1000 = preçoMais1000 + 1
    c = c + 1
    if c == 1:
        produtoBarato = nomeProduto
        preçoMaisBarato = preço

    if preçoMaisBarato > preço:
        preçoMaisBarato = preço
        produtoBarato = nomeProduto

    desejacontinuar = ' '
    while desejacontinuar not in 'SN':
        desejacontinuar = str(input("Você deseja continuar? ")).strip().upper()[0]
    if desejacontinuar == 'N':
        break

print(f"O total da compra foi {somaPreço} Reais ")
print(f"{preçoMais1000} produtos custam mais de 1000 Reais ")
print(f"O produto mais barato é: {produtoBarato} e seu preço é {preçoMaisBarato} Reais ")
