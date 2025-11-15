from collections import UserDict
from datetime import datetime, timedelta
from src.utils.constants import DATE_FORMAT


class AddressBook(UserDict):
    """Stores and manages contact records."""

    def add_record(self, record):
        """Add a record to the address"""
        self.data[record.name.value] = record

    def find(self, name):
        """Find a record by name."""
        record = self.data.get(name, None)
        return record

    def delete(self, name):
        """Delete a record by name."""
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        """
        Returns a list of contacts who should be congratulated
        within the next 7 days, grouped by day.
        """
        today = datetime.today().date()
        upcoming_birthday = []

        for record in self.data.values():
            if not record.birthday or not record.birthday.value:
                continue
            birthday = record.birthday.value.date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today: # already celebrate
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            if today <= birthday_this_year <= today + timedelta(days=7):
                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)
                elif birthday_this_year.weekday() == 6:  
                    congratulation_date = birthday_this_year + timedelta(days=1)
                else:
                    congratulation_date = birthday_this_year
                upcoming_birthday.append({
                'name': record.name.value,
                'congratulation_date': congratulation_date.strftime(DATE_FORMAT)
            })
                
        return upcoming_birthday

    def get_contacts_count(self):
        return len(self.data)
    
    def __str__(self):
        if not self.data:
            return "Address book is empty"

        result = f"Address Book ({len(self.data)} contacts):\n" 
        result += "=" * 50 + "\n"
        for i, record in enumerate(self.data.values(), 1):
            result += f"\n{i}. {record}\n"
            result += "-" * 50 + "\n"
        
        return result

    
    def __repr__(self):
        return f"AddressBook(contacts={len(self.data)})"

