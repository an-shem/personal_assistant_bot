"""
Module for managing a simple address book.

Provides classes for contact fields, individual contact records,
and an address book that stores multiple records.
"""

from src.models.address_book import AddressBook
from src.models.record import Record
from src.utils.parse_input import parse_input
from src.utils.handler_commands import (
    add_contact,
    change_contact,
    show_phone_user,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
)
from src.storage.storage import save_data, load_data


def main():
    # Creating a new address book
    book = load_data()
    print(
        "Welcome to the assistant bot! Type 'Hello' to start or 'Close'/'Exit' to quit."
    )
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Saving address book...")
            save_data(book)
            print("Good bye! See you later!")
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

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
