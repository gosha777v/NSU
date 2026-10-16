# Лучший результат без max
kirill, arina, sergey = map(int, input("Рекорды Кирилла, Арины и Сергея: ").split())
best = kirill
if arina > best:
    best = arina
if sergey > best:
    best = sergey
print(best)
