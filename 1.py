# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:48:44 2026

@author: a3026
"""

import random


def Print_values(a, b, c):
    if a > b:
        if b > c:
            print(a, b, c)
        else:
            if a > c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if b > c:
            if a > c:
                print(b, a, c)
            else:
                print(b, c, a)
        else:
            print(c, b, a)
a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)

print("a =", a)
print("b =", b)
print("c =", c)

print("Output:")
Print_values(a, b, c)