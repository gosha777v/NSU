# Хоккей
first, second = map(int, input("Счёт, например 3:2: ").split(":"))
if first > second:
    print(1)
elif second > first:
    print(2)
else:
    print(0)
