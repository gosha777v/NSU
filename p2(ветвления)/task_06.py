# Дней в году
year = int(input("Год: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(366)
else:
    print(365)
