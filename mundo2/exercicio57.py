sexo = str(input("informe seu sexo [M/F]: ")).strip()
while sexo not in 'MmFf':
    sexo = str(input("Dados invalidos Digite os seu sexo novamente [M/F]: ")).strip()
print("{} sexo registrado com sucesso. ".format(sexo))
