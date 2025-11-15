from src.models.field import Field


class Title(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Note title cannot be empty.")
        if len(value) > 255:
            raise ValueError("Note title cannot exceed 255 characters.")
        super().__init__(value)


class Content(Field):
    def __init__(self, value):
        if len(value) > 255:
            raise ValueError("Note content cannot exceed 255 characters.")
        super().__init__(value)
