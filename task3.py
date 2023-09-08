# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

ticket_number = int(input("Введите номер билета: "))
while ticket_number < 100000 or ticket_number > 999999:
    ticket_number = int(input("Число не 6-значное! Попробуйте еще раз: "))
first_part = ticket_number // 1000
second_part = ticket_number % 1000
first_res = first_part % 10 + first_part // 100 + (first_part // 10) % 10
second_res = second_part % 10 + second_part // 100 + (second_part // 10) % 10
if first_res == second_res:
    print("yes")
else:
    print("no")