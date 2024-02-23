# Homework
#Lesson5
# Task number 1

import random

numbers = [random.randint(-25, 25) for x in range(10)]
print(numbers)


negative_sum = 0
for digit in numbers:
    if digit < 0:
        negative_sum += digit
        print("negative_sum =", negative_sum)


evenumb_sum = 0
for digit in numbers:
    if digit %2 == 0:
        evenumb_sum += digit
        print("evenumb_sum =", evenumb_sum)


oddnumb_sum = 0
for digit in numbers:
    if digit % 2 != 0:
        oddnumb_sum += digit
        print("oddnumb_sum = ", oddnumb_sum)

productionof_3 = 1
for i, digit in enumerate(numbers):
    if i % 3 == 0:
        productionof_3 *= digit
        print("productionof_3 =", productionof_3)

productionof_min_max = 1
min_digit = min(numbers)
max_digit = max(numbers)
for digit in numbers:
    if digit > min_digit and digit < max_digit:
        productionof_min_max *= digit
        print("productionof_min_max= ", productionof_min_max)

interelements_sum = 0
first_element = False
last_element = False
for digit in numbers:
    if digit > 0  and first_element == False:
        first_element = True
    elif first_element == True and digit > 0:
        interelements_sum += digit
    elif first_element == True and digit < 0:
        last_element = True
    elif last_element == True and digit > 0:
        break
    print("interelements_sum= ",interelements_sum)
