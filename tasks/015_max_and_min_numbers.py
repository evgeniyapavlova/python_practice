"""
Пользователь вводит одно число N. 
Далее идут N чисел, записанных на новой строчке каждое. 
Вывести максимальное и минимальное (циклы)

Input: 5 -> 5 1 6 5 9
Output: 1 9
"""

from random import randint

amount_of_numbers = int(input("Input amount of numbers: "))

maxNum, minNum = 0, 0

for i in range(amount_of_numbers):
    num = randint(-50, 50)
    print(num, end=' ')

    if i == 0:
        minNum = num
        maxNum = num

    if num > maxNum:
        maxNum = num

    if num < minNum:
        minNum = num

print()
print(maxNum, minNum)
