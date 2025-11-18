from src.models.field import Field
from src.utils.validation import Validation


class Phone(Field):
    """Represents a phone number with validation using Validation class."""

    def __init__(self, value: str):
        Validation.validate_phone(value)
        normalized_value = Validation.normalize_phone(value)
        super().__init__(normalized_value)

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False

    def __repr__(self):
        return f"Phone({self.value})"
