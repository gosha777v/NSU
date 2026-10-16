# Кольцевая линия метро
n, k, m = map(int, input("N K M: ").split())
if n < 2 or not (1 <= k <= n and 1 <= m <= n):
    print("Некорректные номера станций")
elif k == m:
    print(0)
else:
    distance = k - m
    if distance < 0:
        distance = -distance
    other_distance = n - distance
    if other_distance < distance:
        distance = other_distance
    print(distance - 1)
