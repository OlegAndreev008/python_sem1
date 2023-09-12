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
fib1 = 0
fib2 = 1
fib = 1
count = 2
fib_number = int(input('введите число '))
while fib < fib_number:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    count += 1
if fib == fib_number:
    print(count)
else:
    print('-1')