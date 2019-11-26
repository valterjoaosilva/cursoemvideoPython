produto = input("Informe o produto: ")
preco = float(input("Informe o preço do produto: "))

novoPreco = preco - (preco * 0.05)

print("O produto {}, com o preço {} seu novo preço é: {:.2f}". format(produto, preco, novoPreco))
