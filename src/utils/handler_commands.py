from src.models.notes_book import Note, NotesBook
from src.utils.error_handler import input_error
from src.models.address_book import AddressBook
from src.utils.cli_input import Prompt
from src.models.phone import Phone
from src.models.record import Record


ALL_COMMANDS = ["add-note", "show-notes", "delete-note", "edit-note", "exit", "help"]
PROMPT_TOOL = Prompt(commands=ALL_COMMANDS)


@input_error
def add_contact(args, book: AddressBook):
    """Add a contact or add phone to existing contact."""
    if len(args) != 2:
        # raise an exception so the decorator can catch and format a message
        raise ValueError("Invalid input. Use: Add [name] [phone]")
    name, phone = args
    name = name.capitalize()
    try:
        phone_obj = Phone(phone)
    except ValueError as e:
        raise ValueError(f"Invalid phone number: {e}")
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact '{name}' added."
    else:
        message = f"Contact '{name}' updated."
    if phone:
        record.add_phone(phone_obj.value)
    return message


@input_error
def change_contact(args, book: AddressBook):
    """Usage: change [name] [old_phone] [new_phone]"""
    if len(args) != 3:
        raise ValueError("Usage: change [name] [old_phone] [new_phone]")
    name, old_phone, new_phone = args
    return f"Phone for '{name}' successfully changed."


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
    return str(book)


@input_error
def delete_contact(args, book: AddressBook):
    """Usage: delete [name]"""
    if len(args) != 1:
        raise ValueError("Usage: delete [name]")
    name = args[0]
    return f"Contact '{name}' deleted."


@input_error
def add_birthday(args, book: AddressBook):
    """Usage: add-birthday [name] [DD.MM.YYYY]"""
    if len(args) != 2:
        raise ValueError("Usage: add-birthday [name] [DD.MM.YYYY]")
    name, date_str = args
    return f"Birthday for '{name}' set to {date_str}."


@input_error
def show_birthday(args, book: AddressBook):
    """Usage: show-birthday [name]"""
    if len(args) != 1:
        raise ValueError("Usage: show-birthday [name]")
    name = args[0]
    return f"Birthday for '{name}': [date]"


@input_error
def birthdays(args, book: AddressBook):
    """Usage: birthdays [days] (e.g., birthdays 7)"""
    days = int(args[0]) if args else 7
    return f"Upcoming birthdays in the next {days} days: [list of contacts]"


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

    note = Note(title, content)
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

    new_tags_input = PROMPT_TOOL.ask(
        "Enter new tags (will replace old ones, leave empty to skip): ",
        enable_completion=False,
    ).strip()

    changes = []

    if new_content:
        note.edit_content(new_content)
        changes.append("content")

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
    notes = notes_book.search_notes_by_tag(tag)
    if not notes:
        return f"No notes found with tag '{tag}'."
    return "---Notes found---\n" + "\n\n".join(str(n) for n in notes)
