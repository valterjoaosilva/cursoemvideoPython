from random import choice
aluno1 = input("Digite nome do aluno: ")
aluno2 = input(("Digite o nome do aluno: "))
aluno3 = input("Digite o nome do aluno: ")
aluno4 = input("Digite o nome do aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = choice(lista)
lista
print("O aluno sorteado é: {}, ".format(sorteado))

