# Проверка PIN-кода
pin = input("PIN: ")
if len(pin) != 4:
    print("ERROR")
else:
    a = pin[0]
    b = pin[1]
    c = pin[2]
    d = pin[3]
    if not ("0" <= a <= "9" and "0" <= b <= "9"
            and "0" <= c <= "9" and "0" <= d <= "9"):
        print("ERROR")
    else:
        number = int(pin)
        if a == b or a == c or a == d or b == c or b == d or c == d:
            print("ERROR")
        elif 1900 <= number <= 2050:
            print("ERROR")
        else:
            print("OK")
