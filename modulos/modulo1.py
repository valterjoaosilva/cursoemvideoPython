import math
num = int(input("digite um número: "))
raiz = math.sqrt(num)
print ("A raiz de {} é igual a {}".format(num, raiz))
print ("A raiz de {} é igual a {}".format(num, math.ceil(raiz)))
print ("A raiz de {} é igual a {}".format(num, math.floor(raiz)))
print ("A raiz de {} é igual a {}".format(num, math.trunc(raiz)))