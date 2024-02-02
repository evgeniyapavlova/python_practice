"""
Задача №37. Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""


def reversed(num):
    el = int(input("Input number: "))
    if num == 1:
        return print(el, end=' ')
    reversed(num - 1)
    print(el, end=' ')


n = int(input("Input numbers: "))

reversed(n)
print()
