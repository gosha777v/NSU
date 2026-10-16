import re

name = input("Имя персонажа: ")
if re.fullmatch("Джеймс Бонд|Бонд|агент 007|007", name, re.IGNORECASE):
    print("Верно")
else:
    print("Неверно")
