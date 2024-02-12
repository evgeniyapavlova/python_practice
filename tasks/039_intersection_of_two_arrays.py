"""
Задача №39.
Пользователь вводит размер первого массива – N
и элементы первого массива.
затем размер второго массива M
и элементы второго массива
Нужно вывести те элементы первого массива, которых нет во втором массиве, при этом порядок последовательности сохранить исходный
Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1
"""

from random import randint
n = int(input("Input length of first array: "))
m = int(input("Input length of second array: "))

list_1 = [randint(1,10) for _ in range(n)]
list_2 = [randint(1,10) for _ in range(m)]

print(list_1)
print(list_2)

list_2 = set(list_2)
print(list_2)

# 1
for num in list_1:
    if num not in list_2:
        print(num, end=" ")
print()

# 2
result_list = [num for num in list_1 if num not in list_2]
print(result_list)
