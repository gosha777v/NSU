x, y, n = map(int, input().split())

total = (x * 100 + y) * n

rubles = total // 100
kopecks = total % 100

print(rubles, "руб.", kopecks, "коп.")