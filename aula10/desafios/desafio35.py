reta1 = int(input("Digite Reta1: "))
reta2 = int(input("Digite Reta2: "))
reta3 = int(input("Digite Reta3: "))

if((reta1 > reta2 + reta3) or (reta2 > reta1 + reta3) or (reta3 > reta1 + reta2)):
    print("Não forma um triangulo ")
else:
    print("forma um triangulo ")
