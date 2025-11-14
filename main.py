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
from src.utils.handler_commands import (add_contact, change_contact, delete_contact, show_phone_user, show_all, add_birthday, show_birthday, birthdays, add_note, show_notes, find_note, delete_note, edit_note)
from src.storage.storage import save_data, load_data


def main():
    # Creating a new address book
    book, notes = load_data()


    print(Colorizer.highlight("📘 Welcome to the Assistant Bot!"))
    print(Colorizer.info("Type a command to get started (hello, add, change, phone, all, add-birthday, show-birthday, birthday, add-note, exit)"))

    while True:
        user_input = input(Colorizer.commandline(">>> Enter a command: ")).strip()
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
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone_user(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthday":
            print(birthdays(args, book))
        elif command == "add-note":
            print(add_note(args, notes))
        elif command == "show-notes":
            print(show_notes(args, notes))
        elif command == "find-note":
            print(find_note(args, notes))
        elif command == "edit-note":
            print(edit_note(args, notes))
        elif command == "delete-note":
            print(delete_note(args, notes))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
