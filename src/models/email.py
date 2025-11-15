from src.models.field import Field
from src.utils.validation import Validation


class Email(Field):
    """Represents an email address with validation."""

    def __init__(self, email: str):
        Validation.validate_email(email)
        super().__init__(email)

    def __repr__(self):
        return f"Email(email='{self.value}')"

    def to_dict(self):
        return {"email": self.value}
