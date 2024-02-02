"""
Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

def is_prime(n):
    if n != 2 and n % 2 == 0:
        return 'No'
    for div_i in range(3, int(n ** 0.5) + 1, 2):
        if n % div_i == 0:
            return 'No'
    return 'Yes'


num = int(input("Input number: "))
print(is_prime(num))
