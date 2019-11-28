#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:41:26 2019

@author: valter
"""

numeros = int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")),  \
          int(input("Digite um número: ")), int(input("Digite um número: "))


print(numeros)
print(f"o número 9 apareceu {numeros.count(9)} vez")
if 3 in numeros:
    print(f"O valor 3 aparece pela primeira vez na {numeros.index(3)+1}ª posição.")
else:
    print("O valor 3 não contem na tupla")
print("Os valores pares digitados são: ", end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=',')

