from src.utils.parse_input import parse_input
from src.utils.colorizer import Colorizer
from src.utils.handler_commands import (
    add_contact,
    change_contact,
    delete_contact,
    find_contact,
    show_phone_user,
    add_email,
    add_birthday,
    show_birthday,
    birthdays,
    add_address,
    delete_address,
    find_address_by_city,
    search_address_global,
    show_all_addresses,
    search_contact,
    add_note,
    show_notes,
    find_note,
    delete_note,
    edit_note,
    add_tags_to_note,
    find_notes_by_tag,
    search_by_phone,
)
from src.storage.storage import save_data, load_data
from src.utils.cli_input import Prompt
from src.utils.constants import COMMANDS_INFO
from src.utils.tabulate_helpers import (
    show_commands as print_commands_table,
    show_contacts_table,
)


def main():
    # Creating a new address book
    book, notes = load_data()

    prompt = Prompt(
        commands=COMMANDS_INFO, history_file="src/storage/command_history.txt"
    )

    print(Colorizer.highlight("📘 Welcome to the Assistant Bot!"))
    print_commands_table()

    while True:
        user_input = prompt.ask(">>> Enter command: ").strip()
        if not user_input:
            print(Colorizer.warning("Please enter a valid command."))
            continue
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Colorizer.info("💾 Saving your data..."))
            save_data(book, notes)
            print(Colorizer.success("Data saved. See you later!"))
            break

        elif command == "hello":
            print(Colorizer.info("How can I help you?"))
        elif command in ["help", "commands"]:
            print_commands_table()
        elif command == "add":
            print(Colorizer.success(add_contact(args, book)))
        elif command == "find":
            result = find_contact(args, book)
            # Если вернулся список записей – рисуем таблицу
            if isinstance(result, list):
                show_contacts_table(result)
            # Если вернулась строка (сообщение об ошибке или подсказка использования)
            elif isinstance(result, str):
                print(result)
            # contact = find_contact(args, book)
            # show_contacts_table(contact)
        elif command == "change":
            print(Colorizer.info(change_contact(args, book)))
        elif command == "phone":
            print(Colorizer.highlight(show_phone_user(args, book)))
        elif command == "all":
            contacts = list(book.data.values())
            show_contacts_table(contacts)
        elif command == "delete":
            print(Colorizer.warning(delete_contact(args, book)))
        elif command == "add-birthday":
            print(Colorizer.success(add_birthday(args, book)))
        elif command == "add-email":
            print(Colorizer.success(add_email(args, book)))
        elif command == "add-address":
            print(Colorizer.success(add_address(args, book)))
        elif command == "delete-address":
            print(Colorizer.warning(delete_address(args, book)))
        elif command == "find-city":
            print(Colorizer.info(find_address_by_city(args, book)))
        elif command == "search-address":
            print(Colorizer.info(search_address_global(args, book)))
        elif command == "show-addresses":
            print(Colorizer.highlight(show_all_addresses(args, book)))
        elif command == "search-phone":
            print(Colorizer.info(search_by_phone(args, book)))
        elif command == "show-birthday":
            print(Colorizer.highlight(show_birthday(args, book)))
        elif command == "birthdays":
            print(Colorizer.info(birthdays(args, book)))
        elif command == "search":
            result = search_contact(args, book)
            # Если вернулся список записей – рисуем таблицу
            if isinstance(result, list):
                show_contacts_table(result)
            # Если вернулась строка (сообщение об ошибке или подсказка использования)
            elif isinstance(result, str):
                print(result)
            # contacts = search_contact(args, book)
            # show_contacts_table(contacts)
        elif command == "add-note":
            print(Colorizer.success(add_note(args, notes)))
        elif command == "show-notes":
            result = show_notes(args, notes)
            print(Colorizer.highlight(result))
        elif command == "find-note":
            print(Colorizer.info(find_note(args, notes)))
        elif command == "edit-note":
            print(Colorizer.success(edit_note(args, notes)))
        elif command == "delete-note":
            print(Colorizer.warning(delete_note(args, notes)))
        elif command == "add-tag":
            print(Colorizer.success(add_tags_to_note(args, notes)))
        elif command == "find-tag":
            print(Colorizer.info(find_notes_by_tag(args, notes)))
        else:
            print(
                Colorizer.error(
                    "❌ Invalid command. Type 'info' to see available options."
                )
            )


if __name__ == "__main__":
    main()
