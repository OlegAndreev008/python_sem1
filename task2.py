# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

common = int(input("Сколько журавликов сделали ребята? "))
if common % 6 != 0:
    print("такое условие невозможно")
else:
    pete = sergio = int(common / 6)
    kate = 2 * (pete + sergio)
    print(f"Петя - {pete}, Катя - {kate}, Сережа - {sergio}")