"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""


def sum(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return sum(a, b - 1) + 1
    if b == 0:
        return sum(a - 1, b) + 1
    return sum(a - 1, b - 1) + 1 + 1


# a=3 b=5
# a=2 b=4
# a=1 b=3
# a=0 b=2
# a=0 b=1
# a=0 b=0


c = 10
d = 5
print(sum(c, d))