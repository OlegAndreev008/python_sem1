# Определите, можно ли от шоколадки размером a × b долек отломить c долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.
length = int(input("Количество долек по длине: "))
width = int(input("Количество долек по ширине: "))
break_choco = int(input("Сколько долек хотите отломить?: "))
full_choco = length * width
if (break_choco % length == 0 or break_choco % width == 0) and break_choco <= full_choco:
    print("yes")
else:
    print("no")