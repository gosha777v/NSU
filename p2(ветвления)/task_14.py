# Деньги Гарри Поттера
n = int(input("Количество кнатов: "))
galleons = n // 493
remainder = n % 493
sickles = remainder // 29
knuts = remainder % 29
if galleons > 0:
    print("Галлеоны:", galleons)
if sickles > 0:
    print("Сикли:", sickles)
if knuts > 0:
    print("Кнаты:", knuts)
