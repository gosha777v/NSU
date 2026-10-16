# Диалог с Марком
mark_age = 78  # Возраст из примеров задания.
name = input("Здравствуйте! Как Вас зовут? ")
print(f"Очень приятно, {name}! Меня зовут Марк.")
age = int(input("Сколько Вам лет? "))
if age < mark_age:
    print(f"Да, {name}, я старше Вас на {mark_age - age} лет.")
elif age > mark_age:
    print(f"Да, {name}, Вы старше меня на {age - mark_age} лет.")
else:
    print(f"{name}, мы ровесники!")
answer = input("Вам нравится программировать? ")
if answer == "да" or answer == "Да" or answer == "ДА":
    print("Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.")
elif answer == "нет" or answer == "Нет" or answer == "НЕТ":
    print("Жаль. Я думал, Вы сможете написать интересную программу для меня.")
else:
    print("Я ожидал ответ «да» или «нет».")
