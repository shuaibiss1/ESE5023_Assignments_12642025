# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:57:11 2026

@author: a3026
"""

import random


# 2.1 Generate M1: 5 rows and 10 columns
M1 = []

for i in range(5):
    row = []

    for j in range(10):
        row.append(random.randint(0, 50))

    M1.append(row)


# Generate M2: 10 rows and 5 columns
M2 = []

for i in range(10):
    row = []

    for j in range(5):
        row.append(random.randint(0, 50))

    M2.append(row)


# Print M1
print("M1:")
for row in M1:
    print(row)


# Print M2
print("\nM2:")
for row in M2:
    print(row)


# 2.2 Matrix multiplication
def Matrix_multip(M1, M2):

    # Create a 5 × 5 matrix filled with zeros
    result = []

    for i in range(5):
        row = []

        for j in range(5):
            row.append(0)

        result.append(row)

    # Matrix multiplication
    for i in range(5):
        for j in range(5):
            for k in range(10):

                result[i][j] = result[i][j] + M1[i][k] * M2[k][j]

    return result


M = Matrix_multip(M1, M2)


# Print result
print("\nM1 * M2:")
for row in M:
    print(row)