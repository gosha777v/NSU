# Карусель
n, k, m = map(int, input("Дети N, места K, минуты M: ").split())
if n < 0 or k <= 0 or m <= 0:
    print("Некорректные данные")
elif n == 0:
    print(0)
else:
    sessions = (2 * n + k - 1) // k
    if sessions < 2:
        sessions = 2
    print(sessions * m)
