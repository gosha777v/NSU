def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Деление на ноль невозможно!")
    return x / y

def get_number(prompt):
    """Помогает пользователю ввести корректное число."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"Ошибка! '{input('  Пожалуйста, введите число: ')}' не является числом. Попробуйте снова.")

def main():
    print("=== Python Калькулятор ===")
    
    # Получаем два числа от пользователя с проверкой ввода
    try:
        num1 = get_number("Введите первое число: ")
        num2 = get_number("Введите второе число: ")
        
        # Спрашиваем операцию
        print("\nВыберите операцию:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        
        choice = input("Ваш выбор (1/2/3/4): ")

        # Проверяем выбор пользователя и выполняем расчет
        if choice == '1':
            result = add(num1, num2)
            print(f"\nРезультат: {num1} + {num2} = {result}")
            
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\nРезультат: {num1} - {num2} = {result}")
            
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\nРезультат: {num1} * {num2} = {result}")
            
        elif choice == '4':
            try:
                # Вызываем функцию деления внутри блока try для ловли ошибки нуля
                result = divide(num1, num2)
                print(f"\nРезультат: {num1} / {num2} = {result}")
            except ValueError as e:
                print(f"ОШИБКА ДЕЙСТВИЯ: {e}")
                
        else:
            print("Неверный выбор операции. Пожалуйста, введите 1, 2, 3 или 4.")
            
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем (Ctrl+C).")

if __name__ == "__main__":
    main()