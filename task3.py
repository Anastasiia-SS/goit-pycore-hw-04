import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(directory_path: Path, indent: int = 0):
    try:
        for item in directory_path.iterdir():
            if item.is_dir():
                print("    " * indent + Fore.BLUE + f"[{item.name}]")
                print_directory_structure(item, indent + 1)
            else:
                print("    " * indent + Fore.GREEN + item.name)
    except PermissionError:
        print("    " * indent + Fore.RED + "(Доступ заборонено)")
    except Exception as e:
        print("    " * indent + Fore.RED + f"(Помилка: {e})")

def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "❌ Помилка: Вкажіть шлях до директорії як аргумент.")
        print(Fore.YELLOW + "Приклад: python directory_tree.py C:\\Users\\User\\Documents")
        sys.exit(1)

    path_str = sys.argv[1]
    directory_path = Path(path_str)

    if not directory_path.exists():
        print(Fore.RED + f"❌ Помилка: Шлях '{directory_path}' не існує.")
        sys.exit(1)

    if not directory_path.is_dir():
        print(Fore.RED + f"❌ Помилка: '{directory_path}' не є директорією.")
        sys.exit(1)

    print(Fore.CYAN + f"Структура директорії: {directory_path}\n" + Style.RESET_ALL)
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()