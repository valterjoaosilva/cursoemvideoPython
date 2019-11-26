funcionario = input("Informe o nome do Funcionário: ")
salario = float(input("Informe o salário do funcionário: "))

novoSalario = (salario * 1.15)

print("O funcionário: {} seu salário é {} "
      "com aumento 15% passou a ser {:.2f}".format(funcionario, salario, novoSalario ))
