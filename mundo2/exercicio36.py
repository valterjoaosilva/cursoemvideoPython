valorcasa = int(input("Qual valor da casa: "))
salario = int(input("Qual seu salário: "))
tempopagameto = int(input("Em quantos anos você vai pagar: "))

valorparcela = valorcasa/(tempopagameto * 12)
aprovacao = (valorparcela/salario) * 100

if (aprovacao > 30):
    print("emprestimo negado")
elif(aprovacao <= 30):
    print("emprestimo aprovado\n")
    print("sua parcela é {}".format(valorparcela))
