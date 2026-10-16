m = int(input("Введите вес в фунтах: "))
h = int(input("Введите рост в дюймах: "))

if m <= 0 or h <= 0:
    print("Вес и рост должны быть положительными")
else:
    m1 = m * 0.453592
    h1 = (h * 0.0254) ** 2

    index = m1 / h1

    print("ИМТ =", round(index, 2))

    if index < 16:
        print("Выраженный дефицит массы тела")
    elif index < 18.5:
        print("Недостаточная масса тела")
    elif index < 25:
        print("Норма")
    elif index < 30:
        print("Избыточная масса тела")
    elif index < 35:
        print("Ожирение первой степени")
    elif index < 40:
        print("Ожирение второй степени")
    else:
        print("Ожирение третьей степени")