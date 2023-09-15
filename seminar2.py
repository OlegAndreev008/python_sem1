# факториал числа
# n = int(input("Введите n: "))
# factorial = 1
# help_number = 1
# '''
# n = input("vvedite n")
# while not n.isdigit():
#     print("вы ввели не число")   # проверка на то что мы вводим число
#     n = input("vvedite n")
# n = int(n)
# '''
# while help_number <= n:
#     factorial *= help_number
#     help_number += 1
# print(factorial)

#порядковый номер числа фибоначчи
# fib1 = 0
# fib2 = 1
# fib = 1
# count = 2
# fib_number = int(input('введите число '))
# while fib < fib_number:
#     fib = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib
#     count += 1
# if fib == fib_number:
#     print(count)
# else:
#     print('-1')

# задача с оттепелью
# num = int(input('количество дней: '))
# count = 0
# max_count = 0
# for t in range(num):
#     temp = int(input('введите температуру '))
#     if temp > 0:
#         count += 1
#     else:
#         count = 0
#     if count > max_count:
#         max_count = count
# print(max_count)

# задача с арбузами
# import random
# #watermel = int(input('колво арбузов '))
# max_kg = 3
# min_kg = 12
# num = random.randint(5, 10)
# print(num)
# for i in range(num):
#     kg = random.randint(3, 12)
#     print(kg)
#     if kg > max_kg:
#         max_kg = kg
#     elif kg < min_kg:
#         min_kg = kg
# print(min_kg, max_kg)
    