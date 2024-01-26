"""
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
"""

list_1 = [1, 2, 3, 4, 5]
k = 6 # result = 5

# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10 # result = 9

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8 # result = 8

min_diff = abs(list_1[0] - k)
closest_el = 0

for i in list_1:
    if k == i:
        closest_el = i
        break

    diff = abs(i - k)

    if diff < min_diff:
        min_diff = diff
        closest_el = i

print(closest_el)

