"""
Задача №3. 
В некоторой школе решили набрать три новых математических класса 
и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. 
Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
"""

class1 = int(input("Input amount of studens in class 1: "))
class2 = int(input("Input amount of studens in class 2: "))
class3 = int(input("Input amount of studens in class 3: "))

desks1 = (class1 + 1) // 2
desks2 = (class2 + 1) // 2
desks3 = (class3 + 1) // 2

print(f"Total amount of desks: {desks1 + desks2 + desks3}")
print(f"{desks1 + desks2 + desks3 = }") # знак равно выводит результат выражения
