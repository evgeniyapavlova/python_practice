"""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
"""

n = int(input("Input total amount of paper cranes: "))

amount_petya = n // 6
amount_katya = amount_petya * 4

print(amount_petya, amount_katya, amount_petya)

