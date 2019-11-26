homem = 0
mulher20 = 0
pessoas18 = 0

while True:
    idade = int(input("Digite a Idade: "))
    if idade > 18:
        pessoas18 = pessoas18 +1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Digite o sexo [M/F] ")).strip().upper()[0]
        if sexo in 'M':
            homem = homem + 1
        elif sexo in 'F' and idade < 20:
            mulher20 = mulher20 + 1
    desejacontinuar = ' '
    while desejacontinuar not in 'SN':
        desejacontinuar = str(input("Voce deseja continuar a cadastrar: [S/N]")).strip().upper()[0]
    if desejacontinuar == 'N':
        break

print(f"Sao {pessoas18} com mais de 18 anos, ")
print(f"sao {homem} homens cadastrados")
print(f"Sao {mulher20} mulheres menor de 20 anos")







