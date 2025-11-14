"""
Module for managing a simple address book.

Provides classes for contact fields, individual contact records,
and an address book that stores multiple records.
"""

from src.models.address_book import AddressBook
from src.models.record import Record
from src.utils.parse_input import parse_input
from src.models.notes_book import NotesBook 
from src.utils.colorizer import Colorizer
from src.utils.handler_commands import (add_contact, change_contact, delete_contact, show_phone_user, show_all, add_email, add_birthday, show_birthday, birthdays, add_note, show_notes, find_note, delete_note, edit_note)
from src.storage.storage import save_data, load_data
from src.utils.cli_input import Prompt

COMMANDS = [
    "hello", "add", "change", "phone", "all", "delete", "add-email",
    "add-birthday", "show-birthday", "birthday",
    "add-note", "show-notes", "find-note", "edit-note", "delete-note",
    "exit", "close"
]


def main():
    # Creating a new address book
    book, notes = load_data()

    prompt = Prompt(commands=COMMANDS, history_file="src/storage/command_history.txt")

    print(Colorizer.highlight("📘 Welcome to the Assistant Bot!"))

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
        elif command == "add":
            print(Colorizer.success(add_contact(args, book)))
        elif command == "change":
            print(Colorizer.info(change_contact(args, book)))
        elif command == "phone":
            print(Colorizer.highlight(show_phone_user(args, book)))
        elif command == "all":
            print(Colorizer.highlight(show_all(book)))
        elif command == "delete":
            print(Colorizer.warning(delete_contact(args, book)))
        elif command == "add-birthday":
            print(Colorizer.success(add_birthday(args, book)))
        elif command == "add-email":
            print(Colorizer.success(add_email(args, book)))
        elif command == "show-birthday":
            print(Colorizer.highlight(show_birthday(args, book)))
        elif command == "birthday":
            print(Colorizer.info(birthdays(args, book)))
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
        else:
            print(Colorizer.error("❌ Invalid command. Type 'hello' to see available options."))


if __name__ == "__main__":
    main()
