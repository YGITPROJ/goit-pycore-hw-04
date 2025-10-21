#
#
import os


#
def total_salary(path: str) -> tuple[float, float]:
    # оболонка try для обробки помилок відкриття файлу
    try:
        total_sum = 0.0
        count_lines = 0.0
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) == 2:
                    # оболонка try для обробки помилок строки
                    try:
                        salary_str = parts[1]
                        salary = float(salary_str)
                        total_sum += salary
                        count_lines += 1
                    except ValueError:
                        print(
                            f"Попередження: некоректні дані про зарплату в рядку'{line_number}' : '{line}'. Рядок пропущено."
                        )
                else:
                    print(
                        f"Попередження: некоректний формат рядка '{line_number}' : '{line}'. Рядок пропущено."
                    )
        if count_lines == 0:
            print(
                f"Попередження: файл '{os.path.basename(path)}' порожній або не містить коректних даних."
            )
            return (0.0, 0.0)
        average_salary = total_sum / count_lines
        return (total_sum, average_salary)
    except FileNotFoundError:
        print(f"Помилка: файл за шляхом '{path}' не знайдено.")
        return (0.0, 0.0)
    except IOError as error:
        print(f"Помилка: не вдалося прочитати файл '{path}': {error}")
        return (0.0, 0.0)
    except Exception as error:
        print(f"Сталася неочікувана помилка: {error}")
        return (0.0, 0.0)


#
def main():
    total, average = total_salary("total_salary.txt")
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )


if __name__ == "__main__":
    main()
