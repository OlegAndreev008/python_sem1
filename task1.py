# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.
number = int(input("Введите трехзначное число: "))
while number < 100 or number > 999:
    number = int(input("Число не 3-значное! Попробуйте еще раз: "))
res = number % 10 + number // 100 + (number // 10) % 10
print(f"Сумма чисел числа {number} равна {res}")