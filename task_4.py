#
#


#
# інтерфейс спрощено
#
def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return None, []
    cmd = parts[0].strip().lower()

    args = parts[1:]

    return cmd, args


def add_contact(args, contacts):

    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Contact '{name}' updated."
        else:
            contacts[name] = phone
            return f"Contact '{name}' added."
    except ValueError:
        return "Invalid command format. Use: add [name] [phone]"


def change_contact(args, contacts):

    try:
        name, new_phone = args

        if name in contacts:
            contacts[name] = new_phone
            return f"Contact '{name}' phone updated to {new_phone}."
        else:
            return f"Contact '{name}' not found."

    except ValueError:
        return "Invalid command format. Use: change [name] [new_phone]"


def show_phone(args, contacts):

    try:
        name = args[0]

        if name in contacts:
            return contacts[name]
        else:
            return f"Contact '{name}' not found."

    except IndexError:
        return "Invalid command format. Use: phone [name]"


def show_all(contacts):

    if not contacts:
        return "No contacts found."

    result_lines = []
    for name, phone in contacts.items():
        result_lines.append(f"{name}: {phone}")

    return "\n".join(result_lines)


def main():

    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            response = add_contact(args, contacts)
            print(response)

        elif command == "change":
            response = change_contact(args, contacts)
            print(response)

        elif command == "phone":
            response = show_phone(args, contacts)
            print(response)

        elif command == "all":
            response = show_all(contacts)
            print(response)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
