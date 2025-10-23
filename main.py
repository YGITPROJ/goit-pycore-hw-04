#
#
from task_1 import main as task_1
from task_2 import main as task_2
from task_3 import main as task_3
from task_4 import main as task_4


def main():

    while True:
        print("\n--- Головне меню Домашнього Завдання ---")
        print("Оберіть завдання для запуску:")
        print("1. Завдання 1: Зарплати")
        print("2. Завдання 2: Коти")
        print("3. Завдання 3: Структура директорії")
        print("4. Завдання 4: Бот-асистент")
        print("0. Вихід")

        choice = input("Ваш вибір (0-4): ").strip()

        match choice:
            case "1":
                print("\n[ Завдання 1: Зарплати ]")
                print("-" * 30)
                try:
                    task_1()
                except Exception as e:
                    print(f"Сталася критична помилка: {e}")
                print("-" * 30)
                input("Натисніть Enter, щоб повернутись у меню...")

            case "2":
                print("\n[ Завдання 2: Коти ]")
                print("-" * 30)
                try:
                    task_2()
                except Exception as e:
                    print(f"Сталася критична помилка: {e}")
                print("-" * 30)
                input("Натисніть Enter, щоб повернутись у меню...")

            case "3":
                print("\n[ Завдання 3: Структура директорії ]")
                print("-" * 30)
                try:
                    task_3()
                except Exception as e:
                    print(f"Сталася критична помилка: {e}")
                print("-" * 30)
                input("Натисніть Enter, щоб повернутись у меню...")

            case "4":
                print("\n[ Завдання 4: Бот-асистент ]")
                print("Запуск бота... (введіть 'close' або 'exit', щоб вийти з бота)")
                print("-" * 30)
                try:
                    task_4()
                except Exception as e:
                    print(f"Сталася критична помилка: {e}")

            case "0":

                print("\n--- Роботу завершено. До побачення! ---")
                break
            case _:
                print("\nНеправильний вибір. Будь ласка, введіть число від 0 до 4.")
                input("Натисніть Enter, щоб спробувати ще раз...")


if __name__ == "__main__":
    main()
