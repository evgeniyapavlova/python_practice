"""
Задача №19. Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
на K элементов вправо, K – положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output: [3, 4, 5, 1, 2]
"""

size = int(input("Input amount of elements: "))
k = int(input("Input shift: "))
list_1 = [i for i in range(1, size+1)]
print(list_1)

# 1
print(list_1[-k:] + list_1[:-k])

# 2
for _ in range(k):
    last_num = list_1.pop()
    list_1.insert(0, last_num)

print(list_1)
