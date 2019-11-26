soma = 0
media = 0
homemMaisVelho = 0
nomeHomem = ''
qtdeMulher20 = 0
for c in range(1, 5):
    print("\33[31m_____________{}ª Pessoa ___________\33[m".format(c))
    nome = str(input('Digite nome: ')).strip()
    idade = int(input("Digite a idade: "))
    sexo = str(input('Digite sexo [M/F]: ')).strip()
    soma = soma + idade
    nomeHomem = nome
    if(sexo in 'M' and idade > homemMaisVelho):
        homemMaisVelho = idade
        nomeHomem = nome

    if(idade < 20 and sexo in 'F'):
        qtdeMulher20 = qtdeMulher20 + 1
    if(c == 1 and sexo in 'M'):
        homemMaisVelho = idade


media = soma / 4

print("A média de idade do grupo é: {} Anos ".format(media))
print("Homem mais velho {}, sua idade é: {} anos ".format(nomeHomem, homemMaisVelho))
print("{} mulheres tem menos de 20 anos ".format(qtdeMulher20))