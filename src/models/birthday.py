from src.models.field import Field
from datetime import datetime
from src.utils.constants import DATE_FORMAT

class Birthday(Field):
    def __init__(self, value):
        # Validate and convert string to datetime object
        try:
            self.value = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
         # Display date in readable form
        return self.value.strftime(DATE_FORMAT)