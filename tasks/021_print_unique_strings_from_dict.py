"""
Задача №21. Напишите программу для печати всех уникальных значений в словаре.

Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально. Пользователь его не вводит
"""

list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
              {"VIII": "S007"}]


# Solution 1
unique = set()
for current_dict in list_dicts:
    for value in current_dict.values():
        unique.add(value)
print(unique)

# Solution 2
unique = set()
for current_dict in list_dicts:
    unique.add(*current_dict.values())  # !!! Будет работать только, если внутри каждого словаря один элемент
print(unique)

# Solution 3
unique = set()
for current_dict in list_dicts:
    unique.update(current_dict.values())  # update распаковывает список и добавляет каждый элемент
print(unique)
