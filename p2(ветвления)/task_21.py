# Ход конём
x1, y1, x2, y2 = map(int, input("x1 y1 x2 y2: ").split())
dx = x2 - x1
if dx < 0:
    dx = -dx
dy = y2 - y1
if dy < 0:
    dy = -dy
if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
    print("Неверно")
elif (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("Верно")
else:
    print("Неверно")
