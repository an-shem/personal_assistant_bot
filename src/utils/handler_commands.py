from src.models.notes_book import Note, NotesBook
from src.utils.error_handler import input_error
from src.models.address_book import AddressBook
from src.utils.cli_input import Prompt
from src.models.phone import Phone
from src.models.record import Record
from src.utils.colorizer import Colorizer


ALL_COMMANDS = [
    # system / general
    "hello",
    "help",
    "commands",
    "close",
    "exit",
    # contacts & phones
    "add",
    "change",
    "phone",
    "search-phone",
    "all",
    "delete",
    "add-birthday",
    "show-birthday",
    "birthdays",
    "add-email",
    "search",
    # addresses
    "add-address",
    "delete-address",
    "find-city",
    "search-address",
    "show-addresses",
    # notes
    "add-note",
    "show-notes",
    "find-note",
    "edit-note",
    "delete-note",
    "add-tag",
    "find-tag",
]

PROMPT_TOOL = Prompt(commands=ALL_COMMANDS)


@input_error
def add_contact(args, book: AddressBook):
    """Add a contact or add phone to existing contact."""
    if len(args) != 2:
        raise ValueError("Invalid input. Use: Add [name] [phone]")
    name, phone = args
    name = name.capitalize()
    try:
        phone_obj = Phone(phone)
    except ValueError:
        raise

    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact '{name}' added."
    else:
        message = f"Contact '{name}' updated."
    if phone:
        record.add_phone(phone_obj.value)
        message += f" Phone '{phone_obj.value}'."

    while True:
        email_input = PROMPT_TOOL.ask(
            "Enter email (optional, type 'skip' to omit):", enable_completion=False
        ).strip()
        if not email_input or email_input.lower() == "skip":
            break
        try:
            record.add_email(email_input)
            message += f" Email '{email_input}'."
            break
        except ValueError as e:
            print(Colorizer.warning(f"❌ Email error: {e}. Try again or type 'skip'."))

    while True:
        birthday_input = PROMPT_TOOL.ask(
            "Enter birthday (DD.MM.YYYY, optional, type 'skip' to omit):",
            enable_completion=False,
        ).strip()
        if not birthday_input or birthday_input.lower() == "skip":
            break
        try:
            record.add_birthday(birthday_input)
            message += f" Birthday '{birthday_input}'."
            break
        except ValueError as e:
            print(
                Colorizer.warning(f"❌ Birthday error: {e}. Try again or type 'skip'.")
            )

    add_address_answer = (
        PROMPT_TOOL.ask(
            "Do you want to add an address? (yes/no):", enable_completion=False
        )
        .strip()
        .lower()
    )

    if add_address_answer in ("yes", "y"):
        street = (
            PROMPT_TOOL.ask("Enter street:", enable_completion=False)
            .strip()
            .capitalize()
        )
        if not street:
            print(
                Colorizer.warning("⚠️ Street cannot be empty. Address will be skipped.")
            )
        else:
            city = (
                PROMPT_TOOL.ask("Enter city:", enable_completion=False)
                .strip()
                .capitalize()
            )
            if not city:
                print(
                    Colorizer.warning(
                        "⚠️ City cannot be empty. Address will be skipped."
                    )
                )
            else:
                country = (
                    PROMPT_TOOL.ask("Enter country:", enable_completion=False)
                    .strip()
                    .capitalize()
                )
                if not country:
                    print(
                        Colorizer.warning(
                            "⚠️ Country cannot be empty. Address will be skipped."
                        )
                    )
                else:
                    house_number = (
                        PROMPT_TOOL.ask(
                            "Enter house number (optional, press Enter to skip):",
                            enable_completion=False,
                        ).strip()
                        or None
                    )

                    apartment = (
                        PROMPT_TOOL.ask(
                            "Enter apartment number (optional, press Enter to skip):",
                            enable_completion=False,
                        ).strip()
                        or None
                    )

                    postal_code = (
                        PROMPT_TOOL.ask(
                            "Enter postal code (optional, press Enter to skip):",
                            enable_completion=False,
                        ).strip()
                        or None
                    )

                    try:
                        address = record.add_address(
                            street=street,
                            city=city,
                            country=country,
                            house_number=house_number,
                            apartment=apartment,
                            postal_code=postal_code,
                        )
                        message += f" Address '{address}' added."
                    except Exception as e:
                        print(
                            Colorizer.warning(
                                f"⚠️ Address could not be set: {e}. Continuing..."
                            )
                        )

    return message


@input_error
def change_contact(args, book: AddressBook):
    """Usage: change [name] [old_phone] [new_phone]"""
    if len(args) != 3:
        raise ValueError("Usage: change [name] [old_phone] [new_phone]")
    name, old_phone, new_phone = args
    name = name.capitalize()

    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."

    record.edit_phone(old_phone, new_phone)
    new_phone_obj = Phone(new_phone)
    return f"Phone for '{name}' successfully changed to {new_phone_obj.value}."


@input_error
def show_phone_user(args, book: AddressBook):
    """Usage: phone [name]"""
    if len(args) != 1:
        raise ValueError("Usage: phone [name]")
    name = args[0]
    record = book.find(name)  #
    if not record:
        return f"Contact '{name}' not found."
    if not record.phones:
        return f"Contact '{name}' has no phone numbers saved."

    phone_list = [phone.value for phone in record.phones]

    return f"Phone(s) for '{name}': {', '.join(phone_list)}"


@input_error
def show_all(book: AddressBook):
    """Show all contacts in the address book."""
    if not book.data:
        return "No contacts found."
    result = []
    for record in book.data.values():
        result.append(str(record))
    return "\n".join(result)


@input_error
def delete_contact(args, book: AddressBook):
    """Usage: delete [name]"""
    if len(args) != 1:
        raise ValueError("Usage: delete [name]")
    name = args[0].capitalize()

    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."

    book.delete(name)
    return f"Contact '{name}' deleted."


@input_error
def add_birthday(args, book: AddressBook):
    """Usage: add-birthday [name] [DD.MM.YYYY]"""
    if len(args) != 2:
        raise ValueError("Usage: add-birthday [name] [DD.MM.YYYY]")
    name, date_str = args
    name = name.capitalize()
    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."
    record.add_birthday(date_str)
    return f"Birthday for '{name}' set to {date_str}."


@input_error
def show_birthday(args, book: AddressBook):
    """Usage: show-birthday [name]"""
    if len(args) != 1:
        raise ValueError("Usage: show-birthday [name]")
    name = args[0].capitalize()
    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."

    if not record.birthday or not record.birthday.value:
        return f"Contact '{name}' has no birthday set."

    return f"Birthday for '{name}': {record.birthday.value.strftime('%d.%m.%Y')}"


@input_error
def birthdays(args, book: AddressBook):
    """Usage: birthdays [days] (e.g., birthdays 7)"""
    days = int(args[0]) if args else 7

    upcoming_birthdays = book.get_upcoming_birthdays(days)
    if not upcoming_birthdays:
        return f"No upcoming birthdays in the next {days} days."

    result = f"Upcoming birthdays in the next {days} days:\n"
    for birthday_info in upcoming_birthdays:
        result += f"- {birthday_info['name']}: {birthday_info['congratulation_date']}\n"
    return result.strip()


@input_error
def search_by_phone(args, book: AddressBook):
    """Usage: search-phone [phone]"""
    if len(args) != 1:
        raise ValueError("Usage: search-phone [phone]")
    phone_query = args[0]

    results = book.search_by_phone(phone_query)
    if not results:
        return f"No contacts found with phone: {phone_query}"
    result_str = f"Found {len(results)} contact(s) with phone '{phone_query}':\n"
    result_str += "=" * 50 + "\n"
    for i, record in enumerate(results, 1):
        result_str += f"\n{i}. {record}\n"
        result_str += "-" * 50 + "\n"
    return result_str


@input_error
def add_email(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError("Usage: add-email [name] [email]")
    name, email = args
    name_str = name.capitalize()
    record = book.find(name_str)
    if not record:
        return f"Contact '{name}' not found"

    record.add_email(email)
    return f"Email '{email}' added to contact '{name}'."


@input_error
def add_address(args, book: AddressBook):
    """Usage: add-address [name] — add a new address to the contact."""
    if len(args) != 1:
        raise ValueError("Usage: add-address [name]")

    name = args[0].capitalize()
    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."

    # Interactive address input (same logic as in add_contact)
    street = (
        PROMPT_TOOL.ask("Enter street:", enable_completion=False).strip().capitalize()
    )
    if not street:
        raise ValueError("Street cannot be empty.")

    city = PROMPT_TOOL.ask("Enter city:", enable_completion=False).strip().capitalize()
    if not city:
        raise ValueError("City cannot be empty.")

    country = (
        PROMPT_TOOL.ask("Enter country:", enable_completion=False).strip().capitalize()
    )
    if not country:
        raise ValueError("Country cannot be empty.")

    house_number = (
        PROMPT_TOOL.ask(
            "Enter house number (optional, press Enter to skip):",
            enable_completion=False,
        ).strip()
        or None
    )

    apartment = (
        PROMPT_TOOL.ask(
            "Enter apartment number (optional, press Enter to skip):",
            enable_completion=False,
        ).strip()
        or None
    )

    postal_code = (
        PROMPT_TOOL.ask(
            "Enter postal code (optional, press Enter to skip):",
            enable_completion=False,
        ).strip()
        or None
    )

    address = record.add_address(
        street=street,
        city=city,
        country=country,
        house_number=house_number,
        apartment=apartment,
        postal_code=postal_code,
    )

    return f"Address added for contact '{name}': {address}"


@input_error
def delete_address(args, book: AddressBook):
    """Usage: delete-address [name] — delete one of the contact's addresses."""
    if len(args) != 1:
        raise ValueError("Usage: delete-address [name]")

    name = args[0].capitalize()
    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."

    addresses = record.get_all_addresses()
    if not addresses:
        return f"Contact '{name}' has no addresses."

    print(f"Addresses for contact '{name}':")
    for idx, addr in enumerate(addresses, start=1):
        print(f"  {idx}. {addr}")

    choice_str = PROMPT_TOOL.ask(
        f"Enter the number of the address to delete (1-{len(addresses)}):",
        enable_completion=False,
    ).strip()

    if not choice_str.isdigit():
        raise ValueError("Address number must be an integer.")

    choice = int(choice_str)
    if not (1 <= choice <= len(addresses)):
        raise ValueError(f"Address number must be between 1 and {len(addresses)}.")

    address_to_delete = addresses[choice - 1]

    if record.remove_address(address_to_delete):
        return f"Address #{choice} deleted for contact '{name}'."
    else:
        return "Failed to delete the address. It was not found in the contact."


@input_error
def find_address_by_city(args, book: AddressBook):
    """Usage: find-city [city] — find all addresses in a given city."""
    if len(args) != 1:
        raise ValueError("Usage: find-city [city]")

    city = args[0]
    results = []

    for name, record in book.data.items():
        matches = record.find_by_city(city)
        for addr in matches:
            results.append((name, addr))

    if not results:
        return f"No addresses found in city '{city}'."

    lines = [f"Addresses found in city '{city}':", "-" * 50]
    for contact_name, address in results:
        lines.append(f"{contact_name}: {address}")
    return "\n".join(lines)


@input_error
def search_address_global(args, book: AddressBook):
    """Usage: search-address [query] — search in all addresses of all contacts."""
    if not args:
        raise ValueError("Usage: search-address [query]")

    query = " ".join(args).strip()
    if not query:
        raise ValueError("Search query cannot be empty.")

    results = []

    for name, record in book.data.items():
        matches = record.search_addresses(query)
        for addr in matches:
            results.append((name, addr))

    if not results:
        return f"No addresses found matching '{query}'."

    lines = [f"Addresses matching '{query}':", "-" * 50]
    for contact_name, address in results:
        lines.append(f"{contact_name}: {address}")
    return "\n.join(lines)"


@input_error
def show_all_addresses(args, book: AddressBook):
    """Usage: show-addresses — show all addresses for all contacts."""
    if args:
        raise ValueError("Usage: show-addresses")

    lines = []

    for name, record in book.data.items():
        addresses = record.get_all_addresses()
        if not addresses:
            continue

        lines.append(f"Contact: {name}")
        for idx, addr in enumerate(addresses, start=1):
            lines.append(f"  {idx}. {addr}")
        lines.append("-" * 50)

    if not lines:
        return "There are no addresses saved yet."

    return "\n".join(lines)


@input_error
def search_contact(args, book: AddressBook):
    """Usage: search [query]"""
    if len(args) != 1:
        raise ValueError("Usage: search [query] to find contacts by any field.")

    query = args[0]
    found_records = book.search_all_fields(query)

    if not found_records:
        return f"No contacts found '{query}'."

    output = [f"Found {len(found_records)} contacts '{query}':"]
    for record in found_records:
        output.append(str(record))

    return "\n".join(output)


@input_error
def add_note(args, notes_book: NotesBook):
    """Add a new note with title and text."""

    title = PROMPT_TOOL.ask("Enter a title:", enable_completion=False).strip()
    if not title:
        raise ValueError("The title of the note cannot be empty.")
    if title in notes_book.data:
        return f"Note with title: '{title}' already exists."

    content = PROMPT_TOOL.ask(
        "Enter the text of the note:", enable_completion=False
    ).strip()
    if not content:
        raise ValueError("The text of the note cannot be empty.")

    tags_input = PROMPT_TOOL.ask(
        "Enter tags (optional, separated by spaces/commas):", enable_completion=False
    ).strip()

    tags_message = f" with tags: {tags_input}" if tags_input else ""

    note = Note(title, content, tags=tags_input)
    notes_book.add_note(note)
    return f"Note '{title}' successfully added{tags_message}."


@input_error
def show_notes(args, notes_book: NotesBook):
    """Show all notes."""
    return str(notes_book)


@input_error
def find_note(args, notes_book: NotesBook):
    """Find notes by keyword in title or content."""
    if len(args) == 0:
        keyword = PROMPT_TOOL.ask(
            "Enter keyword to search:", enable_completion=False
        ).strip()
        if not keyword:
            raise ValueError("Keyword cannot be empty.")
    elif len(args) == 1:
        keyword = args[0]
    else:
        raise ValueError("Usage: find-note [keyword]")

    found_notes = notes_book.search_notes_by_keyword(keyword)

    if not found_notes:
        return f"No notes found containing '{keyword}'."

    return "---Notes found---\n" + "\n\n".join(str(n) for n in found_notes)


@input_error
def edit_note(args, notes_book: NotesBook):
    """Edit an existing note by title."""
    title = PROMPT_TOOL.ask(
        "Enter a title for change: ", enable_completion=False
    ).strip()

    note = notes_book.find_note_by_title(title)

    if not note:
        return f"Note with title '{title}' not found."

    new_content = PROMPT_TOOL.ask(
        "Enter new content (leave empty to skip): ", enable_completion=False
    ).strip()

    changes = []

    if new_content:
        note.edit_content(new_content)
        changes.append("content")

    new_tags_input = PROMPT_TOOL.ask(
        "Enter new tags (will replace old ones, leave empty to skip): ",
        enable_completion=False,
    ).strip()

    if new_tags_input:
        note.tags = note._parse_tag(new_tags_input)
        changes.append("tags")

    if not changes:
        return f"Note '{title}' found, but no changes were applied."

    return f"Note with title '{title}' successfully edited: {', '.join(changes)}."


@input_error
def delete_note(args, notes_book: NotesBook):
    """Delete a note by title."""
    title = PROMPT_TOOL.ask(
        "Enter a title for delete: ", enable_completion=False
    ).strip()

    if not title:
        raise ValueError("The note name cannot be empty.")

    note_object = notes_book.find_note_by_title(title)
    if note_object:
        actual_title_key = note_object.title.value
        return notes_book.delete_note(actual_title_key)
    else:
        return f"Note with title: '{title}' not found"


@input_error
def add_tags_to_note(args, notes_book: NotesBook):
    """
    Adds one or more tags to an existing note.
    Accepts title and tags as arguments or interactively.
    """
    if len(args) >= 1:
        title = args[0]
        tags_input = " ".join(args[1:])
    else:
        title = PROMPT_TOOL.ask(
            "Enter the title of the note to add tags to: ", enable_completion=False
        ).strip()
        if not title:
            raise ValueError("Note title cannot be empty.")
        tags_input = ""

    note = notes_book.find_note_by_title(title)
    if not note:
        return f"Note '{title}' not found."

    if not tags_input:
        tags_input = PROMPT_TOOL.ask(
            "Enter tags (separated by spaces/commas):", enable_completion=False
        ).strip()

    if not tags_input:
        return f"No tags were entered for note '{title}'."

    note.add_tags(tags_input)

    return f"Tags successfully added to note '{title}'. New tags: {tags_input}"


@input_error
def find_notes_by_tag(args, notes_book: NotesBook):
    if len(args) != 1:
        raise ValueError("Usage: find-tag [tag]")
    tag = args[0]
    notes = notes_book.search_and_sort_by_tag(tag)
    if not notes:
        return f"No notes found with tag '{tag}'."
    return "---Notes found---\n" + "\n\n".join(str(n) for n in notes)
