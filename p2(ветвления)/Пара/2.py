a,b,c,d = map(int,input("Введите четыре числа через пробел: ").split())

if a > b:
    first = a
else:
    first = b
if c > d:
    second = c
else:
    second = d
if first > second:
    print("Наибольшее число", first)
else:
    print("Наибольшее число", second)