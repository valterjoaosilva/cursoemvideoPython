num1 = int(input("informe o primeiro número: "))
num2 = int(input("informe o segundo número: "))
resultado = 0
somar = 1
multiplicar = 2
maior = 3
novosNúmeros = 4
sair = 5
print('''"#===========#"
      "[1] Somar "
      "[2] Multiplicar"
      "[3] Maior"
      "[4] Novos Números"
      "[5] Sair do Programa"
      "#=============#"''')

opção = int(input("Digite sua opção: "))
while opção != 5:
    if opção == 1:
        resultado = num1 + num2
        print("O resultado de {} + {} = {}".format(num1, num2, resultado))
        print('''"#===========#"
              "[1] Somar "
              "[2] Multiplicar"
              "[3] Maior"
              "[4] Novos Números"
              "[5] Sair do Programa"
              "#=============#"''')
        opção = int(input("Digite a opção: "))

    elif opção == 2:
        resultado = num1 * num2
        print("O resultado de {} x {} = {}".format(num1, num2, resultado))
        print('''"#===========#"
              "[1] Somar "
              "[2] Multiplicar"
              "[3] Maior"
              "[4] Novos Números"
              "[5] Sair do Programa"
              "#=============#"''')
        opção = int(input("Digite a opção: "))


    elif opção == 3:
        if num1 - num2 > 0:
            resultado = num1
            print("Entre {} e {} o maior é {}".format(num1, num2, resultado))
            print('''"#===========#"
                  "[1] Somar "
                  "[2] Multiplicar"
                  "[3] Maior"
                  "[4] Novos Números"
                  "[5] Sair do Programa"
                  "#=============#"''')
            opção = int(input("Digite a opção: "))

        elif num1 - num2 == 0:
            resultado = 'São Iguais'
            print("Entre {} e {} são {}".format(num1, num2, resultado))
            print('''"#===========#"
                  "[1] Somar "
                  "[2] Multiplicar"
                  "[3] Maior"
                  "[4] Novos Números"
                  "[5] Sair do Programa"
                  "#=============#"''')
            opção = int(input("Digite a opção: "))

        else:
            resultado = num2
            print("entre {} e {} o maior é {}".format(num1, num2, resultado))
            print('''"#===========#"
                  "[1] Somar "
                  "[2] Multiplicar"
                  "[3] Maior"
                  "[4] Novos Números"
                  "[5] Sair do Programa"
                  "#=============#"''')
            opção = int(input("Digite a opção: "))

    else:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print('''"#===========#"
              "[1] Somar "
              "[2] Multiplicar"
              "[3] Maior"
              "[4] Novos Números"
              "[5] Sair do Programa"
              "#=============#"''')
        opção = int(input("Digite a opção: "))

print("você saiu do programa")
