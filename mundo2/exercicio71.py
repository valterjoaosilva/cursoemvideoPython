
print("="*30)
print("Banco Valter João")
print("="*30)
saque = int(input("qual o valor a ser sacado R$: "))
valor50 = 50
valor20 = 20
valor10 = 10
valor1 = 1
saque2 = saque // valor50
saque2r = saque % valor50
print(f"total de {saque2} cédulas de R$ {valor50}")
saque3 = saque2r // valor20
saque3r = saque2r % valor20
if saque3 != 0:
    print(f"total de {saque3} cédulas de R$ {valor20}")
saque4 = saque3r // valor10
saque4r = saque3r % valor10
if saque4 != 0:
    print(f"Total de {saque4} cédulas de R$ {valor10}")
saque5 = saque4r// valor1
saque5r = saque4r % valor1
if saque5 != 0:
    print(f"Total de {saque5} cédulas de R$ {valor1}")
print("="*30)


