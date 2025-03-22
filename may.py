import random

def generate_name():
    first_names = ["Олександр", "Марія", "Іван", "Ольга", "Петро", "Наталія"]
    last_names = ["Пригорнёв", "Мельниченко", "Шевченко", "Бондаренко", "Товпашко", "Кравець"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

print(f"Згенероване ім'я: {generate_name()}")
