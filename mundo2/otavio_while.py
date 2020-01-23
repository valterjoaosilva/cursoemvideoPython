número = 10
divisor = 3
resultado = número/divisor
palavra = 'valter joão da silva junior'
print('{:.2f}'.format(resultado))
print(f"{resultado:.2f}")
print(f"{número:0>10}")
print(f"{divisor:0<10}")
print(f'{palavra: >30}')
print(f'{palavra: ^30}')
print(f'{palavra:-^50}')
print(palavra.title())
print(palavra.lower())
print(palavra.capitalize())
print(palavra.isdigit())
print(palavra[3])
print(palavra[:-1])
print(palavra[:2])
print(palavra[7:11], end="")
print(palavra[11:14])

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1

p = 0
while p < 10:
    if p == 3:
        p = p + 1
        break
    print (p)
    p = p + 1
