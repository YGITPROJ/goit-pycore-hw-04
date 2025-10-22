#
#
import sys
from pathlib import Path

try:
    import colorama

    print("colorama є")
except ImportError:
    print("pip install colorama в своєму оточенні")
    sys.exit(1)

# Базові налаштування
colorama.init(autoreset=True)

# def recursive_tree_display(dir_path: Path, prefix: str = ""):
#     pointers = ["┣━ "] * (5) + ["┗━ "]
#     print(pointers)


def get_name_for_sorting(path_item):
    return path_item.name.lower()


def recursive_tree_display(dir_path: Path, prefix: str = ""):

    try:
        items = sorted(
            list(dir_path.iterdir()), key=lambda x: (x.is_file(), x.name.lower())
        )
        # folders = []
        # files = []
        # for item in dir_path.iterdir():
        #     if item.is_file():
        #         files.append(item)
        # else:
        #     folders.append(item)
        # folders.sort(key=get_name_for_sorting)
        # files.sort(key=get_name_for_sorting)
        # items = folders + files
    except PermissionError:
        print(f"{prefix}{colorama.Fore.RED}Відмовлено в доступі.")
        return
    except FileNotFoundError:
        print(f"{prefix}{colorama.Fore.RED}Помилка: Директорію не знайдено.")
        return
    pointers = ["┣━ "] * (len(items) - 1) + ["┗━ "]

    for pointer, item in zip(pointers, items):
        if item.is_dir():
            print(f"{prefix}{pointer}{colorama.Fore.BLUE}{item.name}")
            extension = "┃  " if pointer == "┣━ " else "   "
            recursive_tree_display(item, prefix + extension)

        elif item.is_file():
            print(f"{prefix}{pointer}{colorama.Fore.GREEN}{item.name}")


def visualize_directory(path_str: str):

    dir_path = Path(path_str)

    if not dir_path.exists():
        print(f"{colorama.Fore.RED}Помилка: Шлях '{dir_path}' не існує.")
        return
    if not dir_path.is_dir():
        print(f"{colorama.Fore.RED}Помилка: '{dir_path}' не є директорією.")
        return

    print(f"\n{colorama.Fore.CYAN} {dir_path.resolve().name}")
    recursive_tree_display(dir_path)


def main():
    if len(sys.argv) != 2:
        print(f"{colorama.Fore.RED}Помилка: Неправильне використання.")
        print(
            f"Використання: {colorama.Fore.YELLOW}python task_3.py <шлях_до_директорії>"
        )
        print(
            f"Використання: {colorama.Fore.CYAN}python task_3.py <.> для перегляду кореня скрипту"
        )
        sys.exit(1)  # Виходимо з помилкою

    target_path = sys.argv[1]
    visualize_directory(target_path)


if __name__ == "__main__":
    main()
