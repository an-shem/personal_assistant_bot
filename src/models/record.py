from src.models.phone import Phone
from src.models.name import Name
from src.models.birthday import Birthday
from src.utils.constants import DATE_FORMAT

class Record:
    """Represents a contact record containing a name and a list of phone numbers."""

    def __init__(self, name, phone=None, birthday=None):
        """Initialize the Record with a name and an empty list of phones."""
        self.name = Name(name)
        self.phones = []
        self.birthday = None

        if phone:
            self.add_phone(phone)
        if birthday:
            self.add_birthday(birthday)

    def add_phone(self, number):
        """Add a phone number to the record."""
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        """Remove a phone number from the record."""

        self.phones = list(filter(lambda phone: phone.value != number, self.phones))

    def edit_phone(self, old_number, new_number):
        """Edit a phone number in the record."""

        self.phones = list(
            map(
                lambda phone: Phone(new_number) if phone.value == old_number else phone,
                self.phones,
            )
        )

    def find_phone(self, number):
        """Find a phone number in the record."""

        for phone in self.phones:
            if phone.value == number:
                return phone
        return None
    
    def add_birthday(self, birthday_str):
         """Add a birthday to the contact."""
         self.birthday = Birthday(birthday_str)

    def __str__(self):
        """Return a string representation of the Record."""
        phones = '; '.join(phone.value for phone in self.phones)
        b_day_str = f", birthday: {self.birthday.value.strftime(DATE_FORMAT)}" if self.birthday and self.birthday.value else ""

        return f"Contact name: {self.name.value}, phones: {phones}{b_day_str}"


