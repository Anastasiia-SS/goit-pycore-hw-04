def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue

            name, salary = line.split(',')

            total += float(salary)
            count += 1

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"❌ Файл '{path}' не знайдено. Перевірте шлях до файлу.")
        return (0, 0)
    except PermissionError:
        print(f"❌ Немає доступу до файлу '{path}'.")
        return (0, 0)
    except Exception as e:
        print(f"❌ Невідома помилка при читанні файлу: {e}")
        return (0, 0)

total, average = total_salary("C:\\Users\\fire0\\Desktop\\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")