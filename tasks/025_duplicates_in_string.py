"""
Задача №25. Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию .split()
"""

string_1 = 'a a a b c a a d c d d'
my_list = string_1.split()

# solution 1
result_1 = {}
for el in my_list:
    if el not in result_1:
        result_1[el] = 0
        print(el, end=' ')
    else:
        result_1[el] += 1
        print(f"{el}_{result_1[el]}", end=' ')
print()

# solution 2
result_2 = {}
res_str = ''
for el in my_list:
    if el not in result_2:
        res_str += f'{el} '
    else:
        res_str += f'{el}_{result_2[el]} '
    result_2[el] = result_2.get(el, 0) + 1
res_str = res_str.rsplit()
print(res_str)
