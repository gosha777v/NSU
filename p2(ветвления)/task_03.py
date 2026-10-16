# Да и нет не говорить
print("Вы поедете на бал?")
answer = input("Ответ (строчными буквами): ")
if not (answer == "да" or answer == "Да" or answer == "ДА"
        or answer == "нет" or answer == "Нет" or answer == "НЕТ"):
    print("Верно")
else:
    print("Неверно")
