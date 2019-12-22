'''
N = [4, 5, 6, 8,]
P = [12, 3, 9, 1]
PN = N[:]
PN = PN+[P]
print(PN)

p = []
n = []
pn = []
e = r = i = 0
while i < 5:
    p.append(int(input("Digite um número para lista p  ")))
    n.append(int(input("Digite um número para lista n  ")))
    i+=1
pn.append(p)
pn.append(n)
print(p)
print(n)
print(pn)

while e < len(p):
    pn.append(i)
    e+=1
while r < len(n):
    pn.append(r)
    r+=1
print(pn)
'''
p = []
n = []
pn = []
for i in range(0, 5):
    p.append(int(input("Digite um número para lista p  ")))
    n.append(int(input("Digite um número para lista n  ")))
for i in p:
    pn.append(i)
for i in n:
    pn.append(i)
print(p)
print(n)
print(pn)