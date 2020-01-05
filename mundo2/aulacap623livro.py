'''
L=[15,7,27,39]
p=int( input ("Digite o valor a procurar:"))
achou= False
x=0
while x<len(L):
	if L[x]==p:
		achou = True
		break
	x = x + 1

if achou:
	print ("%d achado na posição %d" % (p,x))
else :
	print ("%d não encontrado" % p)
'''

L = [23, 12, 32, 21]

while True:
    n = int(input("Digite o número que procura: "))
    if n == -1:
        break

    if n in L:
        print(f'O número {n} foi achado na posição')

    else:
        print(f" Número {n} não se encontrado")
