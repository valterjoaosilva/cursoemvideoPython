print('''"===================="
 "SEQUÊNCIA FIBONACCI" 
"===================="''')
fibonacci = int(input("Digite o número: "))
c1 = 0
c2 = 1

print("{} -> {}".format(c1, c2), end=' ')
cont = 3
while cont <= fibonacci:
    c3 = c1 + c2
    print("-> {}".format(c3), end='')
    c1 = c2
    c2 = c3
    cont = cont + 1
print("\n")
print('<>'*10)


