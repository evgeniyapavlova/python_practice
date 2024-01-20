# Задача №1. За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной конструкцией if и циклами.
# Input:
# n = 700км/д
# s= 750км
# Output:
# 2
import math
distance = int(input("Input distance: "))
speed = int(input("Input speed : "))
amountOfDays = math.ceil(distance / speed)
print(amountOfDays)
 