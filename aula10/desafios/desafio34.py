salario = float(input("Digite o Salário: "))
if(salario > 1250.00):
    salario_novo = salario * 1.10

else:
    salario_novo = salario * 1.15

print("O novo salário é: {:.2f} ".format(salario_novo))
