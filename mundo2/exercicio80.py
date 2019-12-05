números = []

for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > números[-1]:
        números.append(n)
    else:
        pos = 0
        while pos < len(números):


            if n <= números[pos]:
                print(pos)
                números.insert(pos, n)
                print(números[pos])
                print(pos)
                print('----')
                break
            pos = pos + 1
            print(números[pos])


print(f"os valores são {números}")

