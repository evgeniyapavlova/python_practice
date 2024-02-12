"""
Задача №49. Дан список размеров(длина, ширина) эллипсов
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
- Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
При решении задачи используйте списочные выражения.
Гарантируется, что самый большой эллипс всего один.
"""

from math import pi


# 1
def find_farthest_orbit(list_of_orbits):
    list_of_ellipsis = [a_b for a_b in list_of_orbits if a_b[0] != a_b[1]]
    list_of_areas = [pi * a * b for a, b in list_of_ellipsis]
    max_area = max(list_of_areas)
    i_max_area = list_of_areas.index(max_area)
    return list_of_ellipsis[i_max_area]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))


# 2
def find_farthest_orbit(list_of_orbits):
    list_of_ellips = list(filter(lambda a_b: a_b[0] != a_b[1], list_of_orbits))
    list_of_areas = list(map(lambda a_b: pi * a_b[0] * a_b[1], list_of_ellips))
    max_area = max(list_of_areas)
    i_max_area = list_of_areas.index(max_area)
    return list_of_ellips[i_max_area]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
