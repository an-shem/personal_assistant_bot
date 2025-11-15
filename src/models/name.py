from src.models.field import Field
from src.utils.validation import Validation

class Name(Field):
    """Represents a field for storing a name, with validation."""

    def __init__(self, name: str):
        Validation.validate_name(name)
        super().__init__(name)