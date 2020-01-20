

soma = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz [l][c] = int(input(f"Digite um número para {l}x{c}"))

for l in range(0, 3):
    for c in range(0, 3):
        if l or c % 2 == 0:
