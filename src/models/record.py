from src.models.phone import Phone
from src.models.name import Name
from src.models.birthday import Birthday
from src.models.email import Email
from src.utils.constants import DATE_FORMAT
from src.models.address import Address

class Record:
    """Represents a contact record containing a name and a list of phone numbers."""

    def __init__(self, name, phone=None, birthday=None, email = None):
        """Initialize the Record with a name and an empty list of phones."""
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None

        if phone:
            self.add_phone(phone)
        if birthday:
            self.add_birthday(birthday)

    def add_phone(self, number):
        """Add a phone number to the record."""
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        """Remove a phone number from the record."""

        self.phones = list(filter(lambda phone: phone.value != number, self.phones))

    def edit_phone(self, old_number, new_number):
        """Edit a phone number in the record."""

        self.phones = list(
            map(
                lambda phone: Phone(new_number) if phone.value == old_number else phone,
                self.phones,
            )
        )

    def find_phone(self, number):
        """Find a phone number in the record."""

        for phone in self.phones:
            if phone.value == number:
                return phone
        return None
    
    def add_birthday(self, birthday_str):
         """Add a birthday to the contact."""
         self.birthday = Birthday(birthday_str)

    def add_email(self, email_str):
        """Add an email to the contact"""
        self.email = Email(email_str)


    def add_record(self, street, city, country, house_number=None, apartment=None, postal_code=None):
        try:
            address = Address(street, city, country, house_number, apartment, postal_code)
            self.data.append(address)
            return address
        except ValueError as e:
            raise ValueError(f"Error creating address: {e}")
    
    def delete_record(self, address):
        if address in self.data:
            self.data.remove(address)
            return True
        return False
    
    def find_by_city(self, city):
        results = []
        city_lower = city.lower()
        for address in self.data:
            if address.city.lower() == city_lower:
                results.append(address)
        return results
    
    def find_by_country(self, country):
        results = []
        country_lower = country.lower()
        for address in self.data:
            if address.country.lower() == country_lower:
                results.append(address)
        return results
    
    def search(self, query):
        query_lower = query.lower()
        results = []
        
        for address in self.data:
            if query_lower in address.street.lower():
                results.append(address)
                continue
            
            if query_lower in address.city.lower():
                results.append(address)
                continue
            
            if query_lower in address.country.lower():
                results.append(address)
                continue
            
            if address.postal_code and query_lower in address.postal_code.lower():
                results.append(address)
                continue
        
        return results
    
    def get_all_contacts(self):
        return self.data.copy()
    

    def __str__(self):
        phones_str = '; '.join([p.value for p in self.phones])
        
        current_email = getattr(self, 'email', None) 
        email_str = f", email: {current_email.value}" if current_email else ""
        
        current_birthday = getattr(self, 'birthday', None)
        if current_birthday and current_birthday.value:
            birthday_str = f", birthday: {current_birthday.value.strftime(DATE_FORMAT)}"
        else:
            birthday_str = ""

        return (f"Contact name: {self.name.value}, phones: {phones_str}"
                f"{email_str}"
                f"{birthday_str}")







