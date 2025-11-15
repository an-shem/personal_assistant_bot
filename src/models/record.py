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
<<<<<<< HEAD
        self.addresses = []
=======
        self.email = None
>>>>>>> 1ab899d8c82ec3291d7628e302816632be738700

        if phone:
            self.add_phone(phone)
        if birthday:
            self.add_birthday(birthday)

    def add_phone(self, number):
        """Add a phone number to the record."""
        phone_obj = Phone(number)
        if any(phone.value == phone_obj.value for phone in self.phones):
            raise ValueError(f"Phone number {phone_obj.value} already exists")
        self.phones.append(phone_obj)

    def remove_phone(self, number):
        """Remove a phone number from the record."""
        try:
            phone_obj = Phone(number)
            number_to_remove = phone_obj.value
        except ValueError:
            number_to_remove = number
        
        original_count = len(self.phones)
        self.phones = [phone for phone in self.phones if phone.value != number_to_remove]
        if len(self.phones) == original_count:
            raise ValueError(f"Phone number {number_to_remove} not found")

    def edit_phone(self, old_number, new_number):
        """Edit a phone number in the record."""
        old_phone_obj = Phone(old_number)
        new_phone_obj = Phone(new_number)

        found = False
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone_obj.value:
                if any(p.value == new_phone_obj.value for p in self.phones if p.value != old_phone_obj.value):
                    raise ValueError(f"Phone number {new_phone_obj.value} already exists")
                self.phones[i] = new_phone_obj
                found = True
                break

        if not found:
            raise ValueError(f"Phone number {old_phone_obj.value} not found") 
        
    def find_phone(self, number):
        """Find a phone number in the record."""
        try:
            phone_obj = Phone(number)
            search_number = phone_obj.value
        except ValueError:
            search_number = number

        for phone in self.phones:
            if phone.value == search_number:
                return phone
        return None
    
    def add_birthday(self, birthday_str):
         """Add a birthday to the contact."""
         self.birthday = Birthday(birthday_str)

    def add_email(self, email_str):
        """Add an email to the contact"""
        self.email = Email(email_str)

<<<<<<< HEAD
        return f"Contact name: {self.name.value}, phones: {phones}{b_day_str}"
    
    def add_addresses(self, street, city, country, house_number=None, apartment=None, postal_code=None):
=======

    def add_address(self, street, city, country, house_number=None, apartment=None, postal_code=None):
>>>>>>> 1ab899d8c82ec3291d7628e302816632be738700
        try:
            address = Address(street, city, country, house_number, apartment, postal_code)
            self.addresses.append(address)
            return address
        except ValueError as e:
            raise ValueError(f"Error creating address: {e}")
    
<<<<<<< HEAD
    def delete_record(self, address):
        if address in self.addresses:
            self.addresses.remove(address)
=======
    def delete_address(self, address):
        if address in self.data:
            self.data.remove(address)
>>>>>>> 1ab899d8c82ec3291d7628e302816632be738700
            return True
        return False
    
    def find_by_city(self, city):
        results = []
        city_lower = city.lower()
        for address in self.addresses:
            if address.city.lower() == city_lower:
                results.append(address)
        return results
    
    def find_by_country(self, country):
        results = []
        country_lower = country.lower()
        for address in self.addresses:
            if address.country.lower() == country_lower:
                results.append(address)
        return results
    
    def search_addresses(self, query):
        query_lower = query.lower()
        results = []
        
        for address in self.addresses:
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
    
    def get_all_addresses(self):
        return self.addresses.copy()
    

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







