def parse_input(user_input):
    
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:]
    return command, args


def add_contact(args, contacts):
    
    if len(args) < 2:
        print("Неправильний формат. Використовуйте: add <ім'я> <номер>")
        return

    name, phone = args[0], args[1]
    contacts[name] = phone
    print("Contact added.")


def change_contact(args, contacts):
    
    if len(args) < 2:
        print("Неправильний формат. Використовуйте: change <ім'я> <новий номер>")
        return

    name, new_phone = args[0], args[1]
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
    else:
        print("Контакт не знайдено.")


def show_phone(args, contacts):
    
    if len(args) < 1:
        print("Неправильний формат. Використовуйте: phone <ім'я>")
        return

    name = args[0]
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Контакт не знайдено.")


def show_all(contacts):
    
    if not contacts:
        print("Контактів поки немає.")
    else:
        print("Усі збережені контакти:")
        for name, phone in contacts.items():
            print(f" - {name}: {phone}")


def main():
    
    contacts = {}

    print("Привіт! Я твій консольний помічник.")
    print("Введи 'close' або 'exit' щоб завершити роботу.\n")

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, contacts)
        elif command == "change":
            change_contact(args, contacts)
        elif command == "phone":
            show_phone(args, contacts)
        elif command == "all":
            show_all(contacts)
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()