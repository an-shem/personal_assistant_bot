import os
import pickle
from src.models.address_book import AddressBook
from src.models.notes_book import NotesBook

CONTACTS_FILE = os.path.join("src", "storage", "addressbook.pkl")
NOTES_FILE = os.path.join("src", "storage", "notes.pkl")


def save_data(book: AddressBook, notes: NotesBook):
    """Save contacts and notes to disk."""
    # Save contacts
    with open(CONTACTS_FILE, "wb") as f:
        pickle.dump(book, f)

    # Save notes
    with open(NOTES_FILE, "wb") as f:
        pickle.dump(notes, f)


def load_data():
    """Load contacts and notes from disk. If missing — create new ones."""
    # Load contacts
    try:
        with open(CONTACTS_FILE, "rb") as f:
            book = pickle.load(f)
    except FileNotFoundError:
        book = AddressBook()

    # Load notes
    try:
        with open(NOTES_FILE, "rb") as f:
            notes = pickle.load(f)
    except FileNotFoundError:
        notes = NotesBook()

    return book, notes