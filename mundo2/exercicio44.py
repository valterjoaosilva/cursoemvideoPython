valorCompra = float(input("Digite o valor da compra: "))
avista = 1
cartaoavista = 2
cartaoparcelado2 = 3
cartaoparcelado3 = 4

formaPagamento = int(input("Digite a forma de pagameto: "))

if (formaPagamento == 1):
    valorAPagar = valorCompra - (valorCompra * 0.10)
    print("valor a pagar é: {}".format(valorAPagar))
elif(formaPagamento == 2):
    valorAPagar = valorCompra - (valorCompra * 0.05)
    print("valor da compra é: {} ".format(valorAPagar))
elif(formaPagamento == 3):
    valorAPagar = (valorCompra * 1)
    print("valor da compra é: {} ".format(valorAPagar))
else:
    valorAPagar = (valorCompra * 1.2)
    print("valor a pagar é: {} ".format(valorAPagar))

