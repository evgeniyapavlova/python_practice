"""
Определите, можно ли от шоколадки размером a × b долек отломить c долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).
Выведите yes или no соответственно.
"""

a = 3
b = 2
c = 4

if c < a and c < b:
    print("no")
elif c > a * b:
    print("no")
elif c % 2 != 0:
    print("no")
else:
    print("yes")
