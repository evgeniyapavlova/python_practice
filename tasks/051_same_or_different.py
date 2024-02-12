"""
Задача №51. Напишите функцию same_by(characteristic, objects), которая проверяет, 
все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. 
Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод:                                               Вывод:
values = [1, 21, 101, 61]                           same
if same_by(lambda x: x % 2 == 0, values):
    print(‘same’)
else:
    print(‘different’)
"""

def same_by(f, values):
    result = set(map(f, values))
    if len(result) < 2:
        return True
    return False

values = [1, 21, 101, 61]                           
if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")

