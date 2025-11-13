from src.models.field import Field
class Phone(Field):
    """Represents a phone number with validation (10 digits)."""
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        # Check if phone number consists of exactly 10 digits
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain exactly 10 digits.")
                                                  