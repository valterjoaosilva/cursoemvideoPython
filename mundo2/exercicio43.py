peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = peso/(altura * altura)

if(imc < 18.5):
    print("Abaixo do peso")
elif(imc >= 18.5 and imc < 25.0):
    print("Peso Ideal")
elif(imc >= 25.0 and imc < 30.0):
    print("sobrepeso")
elif(imc >= 30.0 and imc < 40.0):
    print("Obeso")
else:
    print("Obesidade Morbida")