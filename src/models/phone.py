from src.models.field import Field
from src.utils.validation import Validation

class Phone(Field):
    """Represents a phone number with validation using Validation class."""
    def __init__(self, value: str):
        Validation.validate_phone(value)
        super().__init__(value)
