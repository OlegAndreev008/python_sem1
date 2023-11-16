# Задача 1. с помощью рекурсии выводить N-е число Фибоначчи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# num = int(input('порядковый номер числа '))
# print(fib(num))

# Задача 2. Пр-ма, которая заменяет все макс. значения на миним.
# from random import randint
# mountMark = randint(4, 10)
# marks = [randint(1, 5) for _ in range(mountMark)]
# print(marks)
# def invertMaxMarks(array):
#     max_mark, min_mark = max(array), min(array)
#     for i in range(len(array)):
#         if array[i] == max_mark:
#             array[i] = min_mark
#     return array
# print(invertMaxMarks(marks))

# Задача 3.Написать ф-цию, которая проверяет, является ли число простым.
# from random import randint
# num = randint(1, 50)
# print(num)
# def is_simple(n):
#     if n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     for div in range(3, n):
#         if n % div == 0:
#             return False
#         return True
# is_simple(num)
# if is_simple(num):
#     print('yes')
# else:
#     print('no')

# Задача 4. Дано натуральное число и послед-ть из этого кол-ва элементов.
# Вывести послед-ть в обратном порядке без испол-я циклов и доп массивов.
# def back_seq(n):
#     if n == 0:
#         return ''
#     m = input('print num of seq: ')
#     return back_seq(n - 1) + m + ' '
#
# num = int(input('print mount of nums seq: '))
# print(back_seq(num))