import os


def show_tasks():
    if os.path.exists("справи.txt"):
        with open("справи.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
            if tasks:
                print("\nСписок справ:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\nСписок справ порожній.")
    else:
        print("\nФайл справи.txt не існує.")


def add_task():
    task = input("Яку справу додати? ")
    with open("справи.txt", "a", encoding="utf-8") as file:
        file.write(task + "\n")
    print("Справу додано!")


def clear_tasks():
    open("справи.txt", "w").close()
    print("Всі справи видалено!")


def main():
    while True:
        print("\nМеню:")
        print("1 - Показати всі справи")
        print("2 - Додати нову справу")
        print("3 - Очистити всі справи")
        print("4 - Вийти з програми")

        choice = input("Оберіть дію: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            clear_tasks()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
