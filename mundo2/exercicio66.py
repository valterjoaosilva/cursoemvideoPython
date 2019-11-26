n = 0
soma = 0
s = 0
while n != 999:
    n = int(input("Digite um número (999 para o programa): "))
    if n == 999:
        break
    s = s + 1
    soma = soma + n
print(f"Os {s} números que foram digitados, somam {soma}")

