# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:57:11 2026

@author: a3026
"""

import random
M1 = []
for i in range(5):
    row = []
    for j in range(10):
        row.append(random.randint(0, 50))
    M1.append(row)
M2 = []
for i in range(10):
    row = []
    for j in range(5):
        row.append(random.randint(0, 50))
    M2.append(row)
print("M1:")
for row in M1:
    print(row)
print("M2:")
for row in M2:
    print(row)
def Matrix_multip(M1, M2):
    result = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(0)
        result.append(row)
    for i in range(5):
        for j in range(5):
            for k in range(10):
                result[i][j] = result[i][j] + M1[i][k] * M2[k][j]
    return result
M = Matrix_multip(M1, M2)
print("M1 * M2:")
for row in M:
    print(row)