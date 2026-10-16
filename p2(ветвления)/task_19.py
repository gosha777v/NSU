# Оцепление кварталов
n, m, k = map(int, input("N M K: ").split())
if n > 0 and m > 0 and 0 < k < n * m and (k % n == 0 or k % m == 0):
    print("Можно")
else:
    print("Нельзя")
