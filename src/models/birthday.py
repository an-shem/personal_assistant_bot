from src.models.field import Field
from src.utils.validation import Validation
from datetime import datetime
from src.utils.constants import DATE_FORMAT

class Birthday(Field):
    """Represents a birthday with validation."""
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Birthday must be a string.")
        
        Validation.validate_birthday(value)
        self.value = datetime.strptime(value, DATE_FORMAT)
        super().__init__(self.value)

    def __str__(self):
         # Display date in readable form
        return self.value.strftime(DATE_FORMAT)
    
    def to_dict(self):
        #Return the data in a dictionary format
        return {
            'birthday': self.value.strftime(DATE_FORMAT)
        }
    
    def __repr__(self):
        return f"Birthday(birthday='{self.value.strftime(DATE_FORMAT)}')"
    
