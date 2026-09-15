n = int(input())
c = int(input())
number = int(input())

index = number - 1

page = index // (n * c) + 1
column = index // n % c + 1
row = index % n + 1

print("страница", page, "столбец", column, "строка", row)