while True:
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Помилка: ділення на нуль!")
                continue
            result = num1 / num2
        else:
            print("Невірний оператор!")
            continue

        print(f"Результат: {result}")

    except ValueError:
        print("Помилка: введіть коректні числа!")
        continue

    choice = input("Бажаєте продовжити? (так/ні): ").strip().lower()
    if choice != 'так':
        print("Калькулятор завершив роботу.")
        break