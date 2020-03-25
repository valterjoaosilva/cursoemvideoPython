
cadastro_alunos = {'Primeiro_ano': {'001': 'Julio Gabriel',
                                     'notas001': {'PGS': '7', 'MTM': '5', 'ING': '8'},
                                     '002': 'João Luiz',
                                     'notas002': {'PGS': '7', 'MTM': '5', 'ING': '8'},
                                     '003': 'Antonio Ruiz',
                                     'notas003': {'PGS': '7', 'MTM': '5', 'ING': '8'},
},
                   'Segundo_ano': {'001': 'Francisco Cruz',
                                    'notas001': {'PGS': '7', 'MTM': '5', 'ING': '8'},
                                   '002': 'Tiago Prado',
                                    'notas002': {'PGS': '7', 'MTM': '5', 'ING': '8'},
                                   '003': 'Bernabeu Pinto',
                                    'notas003': {'PGS': '7', 'MTM': '5', 'ING': '8'},
                                   },


}
print()
for pk, pv in cadastro_alunos.items():
    print(f'{pk}' )
    for mk, av in pv.items():
        print(f'{mk}: {av}')


