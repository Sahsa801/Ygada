max_number = float(input("Введіть число 1: "))

for i in range(9):
    num = float(input(f"Введіть число {i+2}: "))
    if num > max_number:
        max_number = num

print(f"Найбільше введене число: {max_number}")