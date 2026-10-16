# Индекс массы тела
weight = float(input("Масса, фунты: "))
height_inches = float(input("Рост, дюймы: "))
if weight <= 0 or height_inches <= 0:
    print("Масса и рост должны быть положительными")
else:
    weight_kg = weight * 0.45359237
    height = height_inches * 0.0254
    bmi = weight_kg / height ** 2
    print(f"ИМТ: {bmi:.2f}")
    if bmi < 16:
        print("выраженный дефицит массы тела")
    elif bmi < 18.5:
        print("недостаточная масса тела")
    elif bmi < 25:
        print("норма")
    elif bmi < 30:
        print("избыточная масса тела")
    elif bmi < 35:
        print("ожирение первой степени")
    elif bmi < 40:
        print("ожирение второй степени")
    else:
        print("ожирение третьей степени")
