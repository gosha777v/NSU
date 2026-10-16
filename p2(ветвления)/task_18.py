# Кирпич и отверстие
a, b = map(float, input("Отверстие A B: ").split())
c, d, e = map(float, input("Кирпич C D E: ").split())
if ((c <= a and d <= b) or (d <= a and c <= b)
        or (c <= a and e <= b) or (e <= a and c <= b)
        or (d <= a and e <= b) or (e <= a and d <= b)):
    print("Пройдёт")
else:
    print("Не пройдёт")
