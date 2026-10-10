# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:20:44 2026

@author: a3026
"""

import random
import matplotlib.pyplot as plt


def Find_expression(x):

    digits = "123456789"
    count = 0

    for n in range(3 ** 8):

        number = n
        expression = digits[0]

        for i in range(8):

            choice = number % 3
            number = number // 3

            if choice == 0:
                expression = expression + digits[i + 1]

            elif choice == 1:
                expression = expression + "+" + digits[i + 1]

            else:
                expression = expression + "-" + digits[i + 1]


        # Calculate the value of the expression
        total = 0
        current_number = ""
        sign = 1

        for i in range(len(expression)):

            if expression[i] == "+":

                total = total + sign * int(current_number)
                current_number = ""
                sign = 1

            elif expression[i] == "-":

                total = total + sign * int(current_number)
                current_number = ""
                sign = -1

            else:

                current_number = current_number + expression[i]


        total = total + sign * int(current_number)


        if total == x:

            print(expression, "=", x)
            count = count + 1


    return count



# 5.1
x = random.randint(1, 100)

print("x =", x)

Find_expression(x)



# 5.2
Total_solutions = []

for i in range(1, 101):

    count = Find_expression(i)

    Total_solutions.append(count)


print("Total_solutions:")
print(Total_solutions)



# Plot
x_values = range(1, 101)

plt.plot(x_values, Total_solutions)

plt.xlabel("Number")
plt.ylabel("Total solutions")
plt.title("Number of solutions from 1 to 100")

plt.show()



# Find maximum
maximum = max(Total_solutions)

print("Maximum number of solutions =", maximum)

for i in range(100):

    if Total_solutions[i] == maximum:

        print("Number with maximum solutions =", i + 1)



# Find minimum
minimum = min(Total_solutions)

print("Minimum number of solutions =", minimum)

for i in range(100):

    if Total_solutions[i] == minimum:

        print("Number with minimum solutions =", i + 1)