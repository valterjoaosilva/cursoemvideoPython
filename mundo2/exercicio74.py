#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:17:17 2019

@author: valter
"""

from random import randint
numeros = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
print(f'{numeros}', end=',')
print()
print(max(numeros))
print(min(numeros))
