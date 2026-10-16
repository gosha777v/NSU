answer = input("Собака короткошерстной породы? ")
if answer == "да":
    answer = input("Рост собаки менее 50 см? ")
    if answer == "да":
        answer = input("У собаки короткий хвост? ")
        if answer == "да":
            print("английский бульдог")
        else:
            answer = input("У собаки длинные уши? ")
            if answer == "да":
                print("гончая")
            else:
                answer = input("У собаки короткое тело? ")
                if answer == "да":
                    print("мопс")
                else:
                    print("чихуахуа")
    else:
        answer = input("Собака весит более 50 кг? ")
        if answer == "да":
            print("датский дог")
        else:
            print("фоксхаунд")
else:
    answer = input("Рост собаки менее 50 см? ")
    if answer == "да":
        answer = input("У собаки доброжелательный характер? ")
        if answer == "да":
            print("кокер-спаниэль")
        else:
            print("ирландский сеттер")
    else:
        answer = input("У собаки рост менее 70 см? ")
        if answer == "да":
            answer = input("У собаки длинные уши? ")
            if answer == "да":
                print("большой вандейский гриффон")
            else:
                print("колли")
        else:
            answer = input("Окрас рыжий с белыми отметинами? ")
            if answer == "да":
                print("сенбернар")
            else:
                answer = input("Белоснежный окрас? ")
                if answer == "да":
                    print("ирландский волкодав")
                else:
                    print("ньюфаундленд")
