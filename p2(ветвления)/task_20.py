# Цвет шахматной клетки
x, y = map(int, input("Столбец и строка (1–8): ").split())
if not (1 <= x <= 8 and 1 <= y <= 8):
    print("Клетки нет на доске")
elif (x + y) % 2 == 0:
    print("Чёрная")
else:
    print("Белая")
