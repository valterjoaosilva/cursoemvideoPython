from math import cos, sin, tan, radians
angulo = float(input("Informe o angulo: "))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print("o angulo {} tem cosseno {} tem seno {} e tangente {}".format(angulo, cosseno, seno, tangente))
