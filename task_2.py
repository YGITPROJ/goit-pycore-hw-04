#
#
import os


#
def get_cats_info(path: str) -> tuple[float, float]:
    cats_list = []
    # оболонка try для обробки помилок відкриття файлу
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) == 3:
                    try:
                        # словник
                        cat_info = {
                            "id": parts[0],
                            "name": parts[1],
                            "age": parts[2],
                        }
                        cats_list.append(cat_info)
                    except Exception as e:
                        # Цей блок малоймовірний при простому
                        # створенні словника, але залишаємо для надійності
                        print(
                            f"Попередження: не вдалося обробити рядок: '{line_number}' : '{line}'. Помилка: {e}"
                        )
                else:
                    # Це спрацює, якщо формат рядка неправильний
                    # (напр. "id,name" або "id,name,age,extra")
                    print(
                        f"Попередження: некоректний формат рядка '{line_number}' : '{line}'. Рядок пропущено."
                    )
        if not cats_list:
            print(
                f"Попередження: файл '{os.path.basename(path)}' порожній або не містить коректних даних."
            )
            return cats_list
        return cats_list
    except FileNotFoundError:
        print(f"Помилка: файл за шляхом '{path}' не знайдено.")
        return cats_list
    except IOError as error:
        print(f"Помилка: не вдалося прочитати файл '{path}': {error}")
        return cats_list
    except Exception as error:
        print(f"Сталася неочікувана помилка: {error}")
        return cats_list


#
def main():
    cats_info = get_cats_info("cats.txt")
    print(cats_info)


if __name__ == "__main__":
    main()
