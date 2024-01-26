"""
Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, 
которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2
Пояснение: (-1 < 5, 2 < 3)
"""

from random import randint

size = int(input("Input amount ef elements in the array: "))

numbers = [randint(-5, 5) for _ in range(size)]
print(numbers)
count = 0

# 1
for i in range(size - 1):
    if numbers[i] < numbers[i + 1]:
        count += 1
print(count)

# 2
print(sum([1 for i in range(size - 1) if numbers[i] < numbers[i + 1]]))
