from src.models.address import Address


class AddressBook:
    def __init__(self):
        self.contacts = []
    
    def add_record(self, street, city, country, house_number=None, apartment=None, postal_code=None):
        try:
            address = Address(street, city, country, house_number, apartment, postal_code)
            self.contacts.append(address)
            return address
        except ValueError as e:
            raise ValueError(f"Error creating address: {e}")
    
    def delete_record(self, address):
        if address in self.contacts:
            self.contacts.remove(address)
            return True
        return False
    
    def find_by_city(self, city):
        results = []
        city_lower = city.lower()
        for address in self.contacts:
            if address.city.lower() == city_lower:
                results.append(address)
        return results
    
    def find_by_country(self, country):
        results = []
        country_lower = country.lower()
        for address in self.contacts:
            if address.country.lower() == country_lower:
                results.append(address)
        return results
    
    def search(self, query):
        query_lower = query.lower()
        results = []
        
        for address in self.contacts:
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
        return self.contacts.copy()
    
    def get_contacts_count(self):
        return len(self.contacts)
    
    def __str__(self):
        if not self.contacts:
            return "Address book is empty"
        
        result = f"Address Book ({len(self.contacts)} addresses):\n"
        result += "=" * 50 + "\n"
        for i, address in enumerate(self.contacts, 1):
            result += f"\n{i}. {address.get_full_address()}\n"
            result += "-" * 50 + "\n"
        
        return result
    
    def __repr__(self):
        return f"AddressBook(contacts={len(self.contacts)})"

