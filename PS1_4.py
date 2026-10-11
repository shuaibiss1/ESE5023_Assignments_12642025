# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:16:54 2026

@author: a3026
"""

import random

def Least_moves(x):
    moves = 0
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x - 1
        moves = moves + 1
    print(moves)
x = random.randint(1, 100)
print("x =", x)
Least_moves(x)