"""
Задача №13. Пользователь вводит число N (1 ≤ N ≤ 10). 
Далее построчно N чисел от -50 до 50. 
Нужно вывести наибольшее количество идущих подряд положительных чисел.

Input: 6 -> -20 30 -40 50 10 -10
Output: 2
"""

from random import randint

amount_of_days = int(input("Input amount of days: "))
count = 0
max_count = count

for i in range(amount_of_days):
    temp = randint(-50, 50)
    print(temp, end=' ')
    if temp > 0:
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 0

print()
print(max_count)