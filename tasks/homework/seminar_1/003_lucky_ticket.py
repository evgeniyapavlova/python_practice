"""
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.

Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет
счастливость билета с номером n и выводит на экран yes или no.
"""

n = int(input("Input number of the ticket: "))

firstHf = n // 1000
secondHf = n % 1000

firstHfSum = firstHf // 100 + (firstHf % 100) // 10 + firstHf % 10
secondHfSum = secondHf // 100 + (secondHf % 100) // 10 + secondHf % 10

if firstHfSum == secondHfSum:
    print("yes")
else:
    print("no")
