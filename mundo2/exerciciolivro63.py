p = []
n = []
pn = []
for i in range(0, 5):
    p.append(int(input("Digite um número para lista p  ")))
    n.append(int(input("Digite um número para lista n  ")))
for i in p:
    if i not in pn:
        pn.append(i)
for i in n:
    if i not in p and i not in pn:
        pn.append(i)
print(p)
print(n)
print(pn)