from pprint import pprint

def get_cats_info(path):

    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            try:
                cat_id, name, age = line.split(',')
                cat_info = {
                    "id": cat_id, 
                    "name": name, 
                    "age": age
                }
                cats.append(cat_info)
            except ValueError:
                print(f"Пропущено некоректний рядок: '{line}'")
                continue
        return cats

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено. Перевірте шлях до файлу.")
        return []
    except PermissionError:
        print(f"Немає доступу до файлу '{path}'.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

cats_info = get_cats_info(r"C:\Users\fire0\Desktop\cats.txt")
pprint(cats_info)