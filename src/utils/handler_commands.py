from src.models.notes_book import Note, NotesBook
from src.utils.error_handler import input_error
from src.models.address_book import AddressBook

@input_error
def add_contact(args, book):
    """Add a contact or add phone to existing contact."""
    pass

@input_error 
def change_contact(args, book: AddressBook):
    """Change an existing phone number for a contact."""
    pass

@input_error 
def change_contact(args, book: AddressBook):
    """Change an existing phone number for a contact."""
    pass

@input_error 
def delete_contact(args, book: AddressBook):
    """Delete  contact."""
    pass

@input_error
def show_phone_user(args, book: AddressBook):
    """Show phone(s) of a given contact."""
    pass

@input_error
def show_all( book: AddressBook):
    """Show all contacts in the address book."""
    pass

@input_error
def show_phone_user(args, book: AddressBook):
    """Show phone(s) of a given contact."""
    pass

@input_error
def add_email(args, book: AddressBook):
    """Add email to an existing contact."""
    pass

@input_error
def add_birthday(args, book: AddressBook):
    """Add birthday to an existing contact."""
    pass

@input_error
def show_birthday(args, book: AddressBook):
    """Show birthday for a contact."""
    pass

@input_error
def birthdays(args, book: AddressBook):
    """Show contacts who have birthdays within the next 7 days."""
    pass

@input_error
def add_note(args, notes_book: NotesBook):
    """Add a new note with title and text."""
    title = input("Enter a title:")
    if not title: 
        raise ValueError("The title of the note cannot be empty.")
    if title in notes_book.data: 
        return f"Note with title: '{title}' already exists."
    content = input("Enter the text of the note:").strip()
    if not content: 
        raise ValueError("The text of the note cannot be empty.")
    note = Note(title, content)
    notes_book.add_note(note)
    return f"Note '{title}' successfully added."

@input_error
def show_notes(args, notes_book: NotesBook):
    """Show all notes."""
    return str(notes_book)

@input_error
def find_note(args, notes_book: NotesBook):
    """Find notes by keyword in title or content."""
    if len(args) != 1:
        raise ValueError("Usage: find-note [keyword]") 
    keyword = args[0]
    found_notes = notes_book.search_notes_by_keyword(keyword)
    if not found_notes:
        return f"No notes found containing '{keyword}'."
    return "---Notes found---\n" + "\n\n".join(str(n) for n in found_notes)

@input_error
def edit_note(args, notes_book: NotesBook):
    """Edit an existing note by title."""
    title = input("Enter a title for change: ")
    new_content = input("Enter new content: ")

    note = notes_book.find_note_by_title(title)

    if note:
        if new_content:
            note.content = new_content

        return (f"Note with title '{title}' successfully edited.")
    else:
        return (f"Note with title '{title}' not found.")


@input_error
def delete_note(args, notes_book: NotesBook):
    """Delete a note by title."""
    title = input("Enter a title for delete: ").strip() 
    
    if not title:
        raise ValueError("The note name cannot be empty.")

    note_object = notes_book.find_note_by_title(title)
    if note_object:
        actual_title_key = note_object.title.value
        return notes_book.delete_note(actual_title_key)
    else:
        return f"Note with title: '{title}' not found"
