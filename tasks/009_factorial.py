"""
Задача №9. По данному целому неотрицательному n вычислите значение
n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while

Input: 5
Output: 120
"""

number = int(input("Input number: "))
factorial = 1
count = 2

while count <= number:
    factorial *= count
    count += 1

print(factorial)
