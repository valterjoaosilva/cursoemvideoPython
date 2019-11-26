from math import pow, sqrt
cat_op = float(input("Informe o cateto oposto: "))
cat_adj = float(input("Informe o cateto adjacente: "))

hipotenusa = sqrt(pow(cat_adj, 2) + pow(cat_op, 2))

print("a hipotenusa é: {:.2f}".format(hipotenusa))

