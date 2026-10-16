# Цифра в последовательности
position = int(input("Номер цифры (1–493): "))
if not (1 <= position <= 493):
    print("Номер должен быть от 1 до 493")
elif position <= 10:
    print(position - 1)
elif position <= 190:
    offset = position - 11
    number = 10 + offset // 2
    if offset % 2 == 0:
        print(number // 10)
    else:
        print(number % 10)
else:
    offset = position - 191
    number = 100 + offset // 3
    digit_index = offset % 3
    if digit_index == 0:
        print(number // 100)
    elif digit_index == 1:
        print(number // 10 % 10)
    else:
        print(number % 10)
