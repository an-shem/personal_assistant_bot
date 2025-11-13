class Address:    
    def __init__(
        self,
        street,
        city,
        country,
        house_number=None,
        apartment=None,
        postal_code=None
    ):
        self._street = street
        self._city = city
        self._country = country
        self._house_number = house_number
        self._apartment = apartment
        self._postal_code = postal_code
    
    @property
    def street(self):
        return self._street
    
    @street.setter
    def street(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Street must be a non-empty string")
        self._street = value.strip()
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("City must be a non-empty string")
        self._city = value.strip()
    
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Country must be a non-empty string")
        self._country = value.strip()
    
    @property
    def house_number(self):
        return self._house_number
    
    @house_number.setter
    def house_number(self, value):
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError("House number must be a non-empty string or None")
        self._house_number = value.strip() if value else None
    
    @property
    def apartment(self):
        return self._apartment
    
    @apartment.setter
    def apartment(self, value):
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError("Apartment number must be a non-empty string or None")
        self._apartment = value.strip() if value else None
    
    @property
    def postal_code(self):
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self, value):
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError("Postal code must be a non-empty string or None")
        self._postal_code = value.strip() if value else None
    
    def get_full_address(self):
        parts = []
        
        if self._street:
            street_part = self._street
            if self._house_number:
                street_part += f", house {self._house_number}"
            if self._apartment:
                street_part += f", apt. {self._apartment}"
            parts.append(street_part)
        
        if self._city:
            parts.append(self._city)
        
        if self._postal_code:
            parts.append(f"({self._postal_code})")
        
        if self._country:
            parts.append(self._country)
        
        return ", ".join(parts)
    
    def __str__(self):
        return self.get_full_address()
    
    def __repr__(self):
        return f"Address(street='{self._street}', city='{self._city}', country='{self._country}')"
    
    def to_dict(self):
        return {
            'street': self._street,
            'house_number': self._house_number,
            'apartment': self._apartment,
            'city': self._city,
            'postal_code': self._postal_code,
            'country': self._country
        }
