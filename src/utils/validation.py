import re
from datetime import datetime

class Validation:
    """Class for validating contact data."""

    @staticmethod
    def validate_name(name: str) -> bool:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        return True
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = r'^\+380\d{9}$'
        if not re.match(pattern, phone):
            raise ValueError("Invalid phone format! Use +380XXXXXXXXX")
        return True
    
    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email format!")
        return True
    
    @staticmethod
    def validate_birthday(birthday: str) -> bool:
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format! Use DD.MM.YYYY")
        return True   