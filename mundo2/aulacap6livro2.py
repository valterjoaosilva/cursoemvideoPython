último = 10
fila = list(range(1, último + 1))
while True :
    print (f"\nExistem {len(fila)} clientes na fila")
    print (f"Fila atual: {fila}")
    print ("Digite F para adicionar um cliente ao fim da fila,")
    print ("ou A para realizar o atendimento. S para sair.")
    operação = str(input("Operação (F, A ou S):"))
    if operação in "Aa":
        if (len(fila)) > 0:
            atendido = fila.pop(0)
            print (f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operação in "Ff":
        último +=1 # Incrementa o ticket do novo cliente
        fila.append(último)
    elif operação in "Ss":
        break

    else:
        print("Operação inválida! Digite apenas F, A ou S!")