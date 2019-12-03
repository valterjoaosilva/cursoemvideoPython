list = 'valter', 35, 'masculino', 'casado', 'josé', 45, 'masculino', 'casado', \
       'vanderlei', 21, 'masculino', 'solteiro', 'eliane', 24, 'feminino', 'solteira', 'marcia', 36, 'feminina', 'solteira', \
       'jordania', 29, 'feminina', 'casada', 'gerson', 59, 'masculino', 'casado', 'josafa', 45, 'masculino', 'solteiro'

for p in range(0, len(list)):
    if p % 4 == 0:
        print(f"\n{list[p]:<10}", end=' ')
    else:
        print(f"{list[p]:->15}", end=', ')

print()
