"""
Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
Примечание: Пользователь может вводить значения списка или список задан изначально
"""

from random import randint

size = int(input("Input size of the list: "))

# list_1 = []
# for i in range(size):
#     num = randint(1, 5)
#     list_1.append(num)

list_1 = [randint(1, 5) for i in range(size)]  # Через генератор списков

# Solution 1
print(len(set(list_1)))

# Solution 2
unique = []
for num in list_1:
    if num not in unique:
        unique.append(num)

print(len(unique))
