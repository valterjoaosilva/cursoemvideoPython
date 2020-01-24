print()
print('Texto Explicativo')
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '2', 'c': '4', },
        'resposta_certa': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': { 'a': '6', 'b': '2', 'c': '4', },
        'resposta_certa': 'a',
    },
}
print()
respostas_certas = 0
respostas_erradas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta:')
    if resposta_usuario == pv['resposta_certa']:
        respostas_certas += 1
        print(f'Você acertou {respostas_certas} repostas')
    else:
        respostas_erradas += 1
        print(f'Você errou {respostas_erradas} respostas')
    print()

if respostas_certas == 2:
    print(f'Você acertou {respostas_certas} respostas e  Tirou Nota (10) Parabéns')
elif respostas_certas == 1:
    print(f'Você acertou apenas {respostas_certas} resposta e tirou nota (5) precisa melhorar')
else:
    print(f'Você não acertou nenhuma resposta tirou nota (zero)')






