n = resultado =0

print('''=========================''')
n = int(input("Qual tabuada você saber? "))
print('''=========================''')
while n != -2:
    c= 1
    while c <= 10:
        resultado = n * c
        print(f"{n} x {c} = {resultado} ")
        c = c + 1
    print('''=========================''')
    n = int(input("Qual tabuada você saber? "))
    print('''=========================''')