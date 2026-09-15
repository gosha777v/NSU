x, y = map(int, input().split())

result = (y != 0 and x % y == 0) or (x != 0 and y % x == 0)

print(int(result))