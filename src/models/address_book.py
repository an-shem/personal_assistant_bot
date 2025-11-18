from collections import UserDict
from datetime import datetime, timedelta
from src.utils.constants import DATE_FORMAT
from src.models.phone import Phone


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

    def search_by_phone(self, phone_query):
        """Search contacts by phone number."""
        results = []
        try:
            phone_obj = Phone(phone_query)
            normalized_query = phone_obj.value
        except ValueError:
            normalized_query = phone_query

        for record in self.data.values():
            for phone in record.phones:
                if normalized_query in phone.value:
                    results.append(record)
                    break
        return results

    def get_upcoming_birthdays(self, days=7):
        """
        Returns a list of contacts who should be congratulated
        within the next specified days (default 7 days.
        """
        today = datetime.today().date()
        upcoming_birthday = []

        for record in self.data.values():
            if not record.birthday or not record.birthday.value:
                continue
            birthday = record.birthday.value.date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:  # already celebrate
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            if today <= birthday_this_year <= today + timedelta(days=days):
                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    congratulation_date = birthday_this_year + timedelta(days=1)
                else:
                    congratulation_date = birthday_this_year
                upcoming_birthday.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime(
                            DATE_FORMAT
                        ),
                    }
                )

        return upcoming_birthday

    def get_contacts_count(self):
        return len(self.data)

    def search_all_fields(self, query: str):
        """Searches for contacts by all fields: name, phone(s), email(s), birthday, and address."""
        query_lower = query.lower().strip()
        results = []

        if not query_lower:
            return results

        query_date = None
        try:
            query_date = datetime.strptime(query_lower, DATE_FORMAT).date()
        except ValueError:
            query_date = None

        for record in self.data.values():

            if query_date:
                if (
                    hasattr(record, "birthday")
                    and record.birthday
                    and record.birthday.value
                ):
                    contact_birthday = record.birthday.value.date()
                    if contact_birthday == query_date:
                        results.append(record)
                        continue

            if query_lower in record.name.value.lower():
                results.append(record)
                continue

            phone_matches = any(
                query_lower in phone.value.lower() for phone in record.phones
            )
            if phone_matches:
                results.append(record)
                continue

            if (
                hasattr(record, "email")
                and record.email
                and query_lower in record.email.value.lower()
            ):
                results.append(record)
                continue

            if (
                hasattr(record, "birthday")
                and record.birthday
                and query_lower in str(record.birthday.value).lower()
            ):
                results.append(record)
                continue

            if getattr(record, "addresses", None):
                for address in record.addresses:
                    full_addr = address.get_full_address().lower()
                    if query_lower in full_addr:
                        results.append(record)
                        break

        return results

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
