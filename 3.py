# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:07:39 2026

@author: a3026
"""

def Pascal_triangle(k):

    row = [1]

    for i in range(1, k):
        new_row = [1]

        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j + 1])

        new_row.append(1)
        row = new_row

    print(row)


Pascal_triangle(100)
Pascal_triangle(200)