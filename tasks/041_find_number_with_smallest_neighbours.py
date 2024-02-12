"""
Задача №41. Пользователь вводит размер массива - N и элементы массива (целые числа).
нужно из этого массива вывести количество элементов, у которых ближайшие соседние элементы меньше самого элемента.

Ввод:           Ввод:
5               5
1 2 3 4 5       1 5 1 5 1
Вывод:          Вывод:
0               2
"""

from random import randint

n = int(input("Input the length of the list: "))

list_num = [randint(1, 5) for _ in range(n)]
print(list_num)

# 1 
count = 0
for i in range(1, len(list_num) -1):
    if list_num[i-1] < list_num[i] and list_num[i+1] < list_num[i]:
        count += 1
print(count)

# 2
print(sum([1 for i in range(1, len(list_num) -1) if list_num[i-1] < list_num[i] and list_num[i+1] < list_num[i]]))
