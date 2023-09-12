# факториал числа
n = int(input("Введите n: "))
factorial = 1
help_number = 1
while help_number <= n:
    factorial *= help_number
    help_number += 1
print(factorial)