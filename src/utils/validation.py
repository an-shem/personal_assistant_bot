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
        """
        Validate Ukrainian phone numbers in multiple formats)
        """
        cleaned_phone = re.sub(r'[\s\-\(\)]', '', phone)

        patterns = [
             r'^\+380\d{9}$',
             r'^0\d{9}$',
             r'^380\d{9}$', 
             r'^80\d{9}$',
        ]
 
        if not any(re.match(pattern, cleaned_phone) for pattern in patterns):
            raise ValueError(
                "Invalid phone format! Supported formats:\n"
                "- +380XXXXXXXXX\n"
                "- 0XXXXXXXXX\n"
                "- 380XXXXXXXXX\n"
                "- 80XXXXXXXXX\n"
                "- With spaces/dashes/parentheses"
                )
        return True
    
    @staticmethod
    def normalize_phone(phone: str) -> str:
        """ 
        Convert any valid Ukrainian phone format to standard +380XXXXXXXXX
        """
        cleaned = re.sub(r'[\s\-\(\)]', '', phone)

        if cleaned.startswith('0'):
            return '+38' + cleaned
        elif cleaned.startswith('80'):
            return '+3' + cleaned
        elif cleaned.startswith('380'): 
            return '+' + cleaned
        elif cleaned.startswith('+380'): 
            return cleaned
        else:
            raise ValueError("Cannot normalise phone number")
    
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