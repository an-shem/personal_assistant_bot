import pickle
from src.models.address_book import AddressBook

FILENAME = "addressbook.pkl"


def save_data(book, filename=FILENAME):
    """Serializing an addressbook object to a file."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename=FILENAME):
    """Deserializing an addressbook object from a file."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
