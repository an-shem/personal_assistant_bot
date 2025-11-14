import re


class Email:
    def __init__(self, email):
      self._email = None
      self.email = email
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Email must be a non-empty string")
        
        email_value = value.strip().lower()
        
        if not self._validate_email(email_value):
            raise ValueError(f"Invalid email address: {value}")
        
        self._email = email_value
    
    @staticmethod
    def _validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def __str__(self):
        return self._email
    
    def __repr__(self):
        return f"Email(email='{self._email}')"
    
    def to_dict(self):
        return {
            'email': self._email
        }

